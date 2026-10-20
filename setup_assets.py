#!/usr/bin/env python3
"""
Download the MediaPipe browser runtime and hand model into this website.
Run once on a Windows/Mac/Linux computer with internet access.
Afterwards, upload the complete School_VR_Tour_Web_App folder to GitHub Pages.
"""
import io, os, sys, tarfile, urllib.request, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
VENDOR = os.path.join(ROOT, "vendor", "tasks-vision")
WASM = os.path.join(VENDOR, "wasm")
MODEL_DIR = os.path.join(ROOT, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "hand_landmarker.task")

PACKAGE_URL = "https://registry.npmjs.org/@mediapipe/tasks-vision/-/tasks-vision-0.10.22.tgz"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"

def download(url, label):
    print(f"Downloading {label} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "School-VR-Tour-Setup/1.0"})
    with urllib.request.urlopen(req, timeout=120) as response:
        return response.read()

def main():
    try:
        os.makedirs(WASM, exist_ok=True)
        os.makedirs(MODEL_DIR, exist_ok=True)

        archive = download(PACKAGE_URL, "MediaPipe Tasks Vision 0.10.22")
        print("Extracting MediaPipe JavaScript bundle and WASM runtime ...")
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as tar:
            wanted = ("package/vision_bundle.mjs",)
            for member in tar.getmembers():
                name = member.name.replace("\\", "/")
                if name in wanted:
                    member.name = os.path.basename(name)
                    tar.extract(member, VENDOR, filter="data")
                elif name.startswith("package/wasm/") and not member.isdir():
                    relative = name[len("package/"):]
                    member.name = relative
                    tar.extract(member, VENDOR, filter="data")

        bundle = os.path.join(VENDOR, "vision_bundle.mjs")
        if not os.path.isfile(bundle) or not os.listdir(WASM):
            raise RuntimeError("MediaPipe package extraction was incomplete. Delete vendor/tasks-vision and retry.")

        model = download(MODEL_URL, "hand landmark model")
        if len(model) < 1_000_000:
            raise RuntimeError("Downloaded model file is unexpectedly small; check your internet connection.")
        with open(MODEL_PATH, "wb") as f:
            f.write(model)

        print("\nSUCCESS: local hand-mesh assets are ready.")
        print(f"  JS bundle: {bundle}")
        print(f"  WASM files: {WASM}")
        print(f"  Model: {MODEL_PATH} ({len(model):,} bytes)")
        print("\nNext: upload the entire School_VR_Tour_Web_App folder to the ROOT of your GitHub Pages repository.")
        print("Keep the vendor/ and models/ folders. Do not upload just index.html.")
    except Exception as e:
        print("\nSETUP FAILED:", e)
        print("Check that this computer has internet access, then run setup_assets.bat again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
