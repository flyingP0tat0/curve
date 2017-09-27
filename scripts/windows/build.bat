pyinstaller ^
  src/main.py ^
  --onefile ^
  --add-data="config/config.yml:/" ^
  --add-data="config/color.yml:/" ^
  --name="curve" ^
  --windowed ^
  --icon=img/icon.ico ^
  --clean
