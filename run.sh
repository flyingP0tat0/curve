#!/bin/sh

ABSOLUTE_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P )

function help {
  echo "curve tool"
  echo ""
  echo "  usage: sh run.sh <command>"
  echo ""
  echo "  available commands:"
  echo "    run          - run the game"
  echo "    run server   - run the server (requires rust and cargo)"
  echo "    build        - build the game for this platform"
  echo "    build server - build the server (requires rust and cargo)"
  echo "    setup        - install dependencies"
  echo "    setup dev    - install development dependencies"
  echo "    test         - run unit tests"
  echo "    test server  - run unit tests for the server (requires rust and cargo)"
  echo "    lint         - lint the code"
  echo "    check server - check server (requires rust and cargo)"
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
  case "$2" in
  ("")
    pyinstaller \
    src/main.py \
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
  
  ("server")
    $(cd ${ABSOLUTE_PATH}/server && cargo build --release)
    mv ${ABSOLUTE_PATH}/server/target/release/server ${ABSOLUTE_PATH}/dist/server
    ;;

  *)
    help
    ;;
  esac
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
  case "$2" in
  ("")
    python3 -m unittest discover -s ${ABSOLUTE_PATH}/test -p "*_test.py"
    ;;
  
  ("server")
    $(cd ${ABSOLUTE_PATH}/server && cargo test)
    ;;

  *)
    help
    ;;
  esac
  ;;

("lint")
  help # TODO: implement linting
  ;;

("check"):
  case "$2" in
  ("server")
    $(cd ${ABSOLUTE_PATH}/server && cargo check)
    ;;

  *)
    help
    ;;
  esac
  ;;


("clean")
  rm -rf ${ABSOLUTE_PATH}/dist/*
  rm -rf ${ABSOLUTE_PATH}/build/*
  rm -rf ${ABSOLUTE_PATH}/**/__pychache__ # TODO: not working
  rm -f ${ABSOLUTE_PATH}/**.pyc
  rm -f ${ABSOLUTE_PATH}/*.spec
  rm -rf ${ABSOLUTE_PATH}/**/target
  rm -f ${ABSOLUTE_PATH}/**/Cargo.lock
  ;;

("help")
  help
  ;;

*)
  help
  ;;
esac
