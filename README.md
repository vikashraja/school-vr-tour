# School 360° VR Tour — Web App

This is the web version of the School VR Tour, with all 11 supplied panorama photos bundled locally.

## Quick test on your computer
1. Extract this ZIP.
2. Open the extracted folder.
3. Double-click `index.html` to try the viewer. If the browser blocks local image loading, use the local server method below.

## Recommended local server
Install Python if needed, open Command Prompt in this folder, then run:
    python -m http.server 8000
Open http://localhost:8000 in your browser.

## Open on your Redmi phone
For device motion/orientation and VR features, host this folder on an HTTPS static web host (for example GitHub Pages or Netlify), then open the HTTPS URL in Chrome on Android. Local `file://` pages and plain HTTP may restrict motion/VR APIs. Allow motion/orientation permissions if prompted and tap Enter VR.

## Features
- 11 bundled panorama photos (no photo hosting needed)
- Location dropdown and Previous/Next controls
- 360° look-around using mouse/touch; phone orientation where supported
- Split-screen VR mode for a Cardboard-style headset
- Gaze markers for switching between adjacent views
- Optional spoken narration using browser speech synthesis

## Important limitations
- The A-Frame library is loaded from its public CDN, so the viewer needs an internet connection to start. The panorama images themselves are included in this ZIP.
- VR/orientation support varies by browser and phone. HTTPS hosting is recommended.
- The panorama photos provide 360° viewing, not true stereoscopic 3D depth.
- Location labels are generic (“School View 01” through “School View 11”) because specific room/location names were not provided.
