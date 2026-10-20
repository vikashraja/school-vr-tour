#!/usr/bin/env python3
"""Prepare all local MediaPipe assets for the School VR Tour.
Run this once on a computer with internet access, then upload the complete project to GitHub Pages.
"""
import io, json, os, shutil, sys, tarfile, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
VENDOR = os.path.join(ROOT, 'vendor', 'tasks-vision')
WASM = os.path.join(VENDOR, 'wasm')
MODEL_DIR = os.path.join(ROOT, 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'hand_landmarker.task')
VERSION = '0.10.21'
REGISTRY = f'https://registry.npmjs.org/@mediapipe%2ftasks-vision/{VERSION}'
MODEL_URL = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'

def fetch(url, label):
    print('Downloading ' + label + '...', flush=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'School-VR-Tour-Asset-Setup/2.0'})
    with urllib.request.urlopen(req, timeout=180) as response:
        return response.read()

def main():
    try:
        os.makedirs(VENDOR, exist_ok=True)
        os.makedirs(WASM, exist_ok=True)
        os.makedirs(MODEL_DIR, exist_ok=True)
        metadata = json.loads(fetch(REGISTRY, f'MediaPipe package metadata ({VERSION})').decode('utf-8'))
        tarball_url = metadata.get('dist', {}).get('tarball')
        if not tarball_url:
            raise RuntimeError('npm metadata did not provide a package download URL.')
        archive = fetch(tarball_url, 'MediaPipe JavaScript bundle and WASM files')
        extracted = []
        with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as tar:
            for member in tar.getmembers():
                name = member.name.replace('\\', '/')
                if member.isdir():
                    continue
                if name == 'package/vision_bundle.mjs':
                    dest = os.path.join(VENDOR, 'vision_bundle.mjs')
                elif name.startswith('package/wasm/'):
                    rel = name[len('package/wasm/'):]
                    if not rel or rel.startswith('/') or '..' in rel.split('/'):
                        continue
                    dest = os.path.join(WASM, *rel.split('/'))
                else:
                    continue
                src = tar.extractfile(member)
                if src is None:
                    continue
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with src, open(dest, 'wb') as out:
                    shutil.copyfileobj(src, out)
                extracted.append(dest)
        bundle = os.path.join(VENDOR, 'vision_bundle.mjs')
        wasm_files = [p for p in extracted if os.path.dirname(p) == WASM]
        if not os.path.isfile(bundle) or not wasm_files:
            raise RuntimeError('Package download succeeded but required bundle/WASM files were not found.')
        model = fetch(MODEL_URL, 'Hand Landmarker model')
        if len(model) < 1_000_000:
            raise RuntimeError(f'Model download was unexpectedly small ({len(model)} bytes).')
        with open(MODEL_PATH, 'wb') as f:
            f.write(model)
        # Remove obsolete placeholders from earlier versions.
        for path in [os.path.join(WASM, 'PUT_WASM_FILES_HERE.txt'), os.path.join(MODEL_DIR, 'PUT_MODEL_HERE.txt')]:
            if os.path.exists(path): os.remove(path)
        print('\nSUCCESS: local hand-mesh assets are ready.', flush=True)
        print('Bundle: ' + os.path.relpath(bundle, ROOT), flush=True)
        print('WASM files: ' + str(len(wasm_files)), flush=True)
        print('Model size: {:,} bytes'.format(len(model)), flush=True)
        print('\nNow upload ALL contents of this folder to the ROOT of your GitHub repository.', flush=True)
        print('Keep the folder paths exactly as they are: vendor/tasks-vision and models.', flush=True)
    except Exception as exc:
        print('\nSETUP FAILED: ' + repr(exc), flush=True)
        print('Check internet access. If this is a network/DNS error, try another network and run again.', flush=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
