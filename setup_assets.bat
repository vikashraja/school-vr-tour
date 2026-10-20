@echo off
title School VR Tour - Download Local Hand Mesh Assets
py -3 setup_assets.py
if errorlevel 1 (
  echo.
  echo Setup failed. Read the error above.
) else (
  echo.
  echo Assets downloaded. You can now upload the whole website folder to GitHub.
)
pause
