where /q python3

IF ERRORLEVEL 1 (
  where /q python
  
  IF ERRORLEVEL 1 (
    ECHO No python found.
    EXIT /B
  )
  ELSE (
    python ../../src/main.py
  )
)
ELSE (
  python3 ../../src/main.py
)
