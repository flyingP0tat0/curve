:help
  echo curve tool
  echo 
  echo   usage: sh run.sh <command>
  echo 
  echo   available commands:
  echo     run          - run the game
  echo     build        - build the game for this platform
  echo     setup        - install dependencies
  echo     setup dev    - install development dependencies
  echo     test         - run unit tests
  echo     lint         - lint the code
  echo     clean        - clean up all temporary files
  echo     help         - show this help
  exit /B 0


IF "%1" == "run" (
  python3 src/main.py
  GOTO exit
)

IF "%1" == "build" (
  python3 src/main.py
  GOTO exit
)

IF "%1" == "setup" (
  IF "%2" == "" (
    pip3 install -r requirements.txt
    GOTO exit
  )
  IF "%2" == "dev" (
    pip3 install -r requirements_dev.txt
    GOTO exit
  )
)

IF "%1" == "test" (
  python3 -m unittest discover -s test -p "*_test.py"
  GOTO exit
)

IF "%1" == "lint" (
  pylint src/*.py
  GOTO exit
)

IF "%1" == "clean" (
  echo "ToDo"
  GOTO exit
)

IF "%1" == "help" (
  help
  GOTO exit
)

help
:exit
