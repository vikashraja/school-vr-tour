# School VR Tour + Local Hand Mesh (Android)

This version keeps the school tour and Hand Mesh in one web interface. Hand tracking runs in the Android browser using MediaPipe JavaScript; no Python process or Windows laptop is needed during normal use.

## One-time setup (use a Windows laptop with internet)

1. Extract this ZIP.
2. Open `School_VR_Tour_Web_App`.
3. Double-click `setup_assets.bat`.
   - If Windows says Python is missing, install Python 3 from https://www.python.org/downloads/ and select **Add Python to PATH**, then double-click the BAT again.
   - This script downloads the MediaPipe JavaScript bundle, WASM runtime files, and hand model into local folders.
4. Wait until it says `SUCCESS`.
5. Upload the **entire contents** of `School_VR_Tour_Web_App` to the root of your existing GitHub Pages repository, preserving folders:
   - `index.html`
   - `photos/`
   - `vendor/tasks-vision/` (created by the setup script)
   - `models/hand_landmarker.task` (created by the setup script)
6. Commit the upload and wait for GitHub Pages to publish.
7. On Android, open your HTTPS tour site in Chrome, allow camera permission, and tap **Hand Mesh**.

## Important

- The download/setup computer is only needed to fetch the files and upload them. The hand mesh runs on the Android phone.
- The hand-mesh code uses local paths and does not load MediaPipe from `esm.sh` or `jsDelivr`.
- This bundles MediaPipe and its model locally, but other tour components (for example A-Frame if referenced from a CDN) may still require internet. The whole website is not guaranteed to work fully offline until all remaining external assets are also bundled and the site is installed/cached appropriately.
- GitHub Pages must serve the site over HTTPS for camera access.
- Do not upload just `index.html`; the `vendor` and `models` folders are required.
