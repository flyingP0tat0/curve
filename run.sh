#!/bin/sh

ABSOLUTE_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P )

function help {
  echo "curve tool"
  echo ""
  echo "  usage: sh run.sh <command>"
  echo ""
  echo "  available commands:"
  echo "    run          - run the game"
  echo "    build        - build the game for this platform"
  echo "    setup        - install dependencies"
  echo "    setup dev    - install development dependencies"
  echo "    test         - run unit tests"
  echo "    lint         - lint the code"
  echo "    clean        - clean up all temporary files"
  echo "    help         - show this help"
}

case "$1" in
("run")
  case "$2" in
  ("")
    python3 ${ABSOLUTE_PATH}/src/main.py
    ;;
  
  ("server")
    $(cd ${ABSOLUTE_PATH}/server && cargo run)
    ;;

  *)
    help
    ;;
  esac
  ;;

("build")
  pyinstaller \
  ${ABSOLUTE_PATH}/src/main.py \
  --name="curve" \
  --onefile \
  --windowed \
  --add-data="config/**:/config/" \
  --add-data="audio/**:/config/" \
  --add-data="img/**:/img/" \
  --add-data="fonts/**:/fonts/" \
  --icon=img/icon.ico \
  --workpath=${ABSOLUTE_PATH}/build \
  --distpath=${ABSOLUTE_PATH}/dist \
  --clean \
  --strip
  ;;

("setup")
  case "$2" in
  ("")
    pip3 install -r ${ABSOLUTE_PATH}/requirements.txt
    ;;
  
  ("dev")
    pip3 install -r ${ABSOLUTE_PATH}/requirements_dev.txt
    ;;

  *)
    help
    ;;
  esac
  ;;

("test")
  python3 -m unittest discover -s ${ABSOLUTE_PATH}/test -p "*_test.py"
  ;;

("lint")
  python3 -m pylint ${ABSOLUTE_PATH}/src/*.py
  ;;

("clean")
  rm -rf ${ABSOLUTE_PATH}/dist/*
  rm -rf ${ABSOLUTE_PATH}/build/*
  rm -rf ${ABSOLUTE_PATH}/**/__pychache__ # TODO: not working
  rm -f ${ABSOLUTE_PATH}/**.pyc
  rm -f ${ABSOLUTE_PATH}/*.spec
  ;;

("help")
  help
  ;;

*)
  help
  ;;
esac
