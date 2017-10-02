pyinstaller ^
  src/main.py ^
  --onefile ^
  --add-data="config/config.yml:/" ^
  --name="curve" ^
  --windowed ^
  --icon=img/icon.ico ^
  --clean
