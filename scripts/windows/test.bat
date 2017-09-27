where /q python3

IF ERRORLEVEL 1 (
  where /q python
  
  IF ERRORLEVEL 1 (
    ECHO No python found.
    EXIT /B
  )
  ELSE (
    python -m unittest discover -s ../../test -p "*_test.py"
  )
)
ELSE (
  python3 -m unittest discover -s ../../test -p "*_test.py"
)