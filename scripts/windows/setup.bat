where /q pip3

IF ERRORLEVEL 1 (
  where /q pip
  
  IF ERRORLEVEL 1 (
    ECHO No pip found.
    EXIT /B
  )
  ELSE (
    pip install -r ../../requirements.txt
  )
)
ELSE (
  pip3 install -r ../../requirements.txt
)
