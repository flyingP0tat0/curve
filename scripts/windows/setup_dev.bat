where /q pip3

IF ERRORLEVEL 1 (
  where /q pip
  
  IF ERRORLEVEL 1 (
    ECHO No pip found.
    EXIT /B
  )
  ELSE (
    pip install ../../requirements_dev.txt
  )
)
ELSE (
  pip3 install ../../requirements_dev.txt
)