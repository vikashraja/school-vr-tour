# School VR Tour — Hand Mesh (GitHub Pages)

## Important: prepare the runtime before uploading

The MediaPipe JavaScript bundle, WASM runtime, and hand model are downloaded by the setup script. They are not placeholder files and should not be manually renamed or fabricated.

### Windows
1. Extract this ZIP.
2. Open `School_VR_Tour_Web_App`.
3. Double-click `setup_assets.bat` and wait for `SUCCESS: local hand-mesh assets are ready.`
4. If setup fails, do not upload yet. Read the displayed error and try a network with working access to npmjs.org and storage.googleapis.com.
5. Upload **all contents inside** `School_VR_Tour_Web_App` to the root of your existing `school-vr-tour` GitHub repository. Upload folders recursively and preserve their names.
6. Wait for GitHub Pages to deploy, then open the website in Android Chrome and grant camera permission.

### Required final paths

- `index.html`
- `photos/` (all panorama images)
- `models/hand_landmarker.task`
- `vendor/tasks-vision/vision_bundle.mjs`
- `vendor/tasks-vision/wasm/` (all files created by the setup script)

Do not upload `vision_bundle.js` into the `wasm` folder. The correct bundle is `vision_bundle.mjs` inside `vendor/tasks-vision/`.

The setup script requires Python 3 and internet access on the computer used to prepare the project. At runtime, hand mesh runs in the phone browser; no separate Python app is needed.
