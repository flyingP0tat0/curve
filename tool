#!/bin/bash

ABSOLUTE_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P )

GREY="\e[0;37m"
MAGENTA="\e[0;35m"
RED="\e[0;31m"
GREEN="\e[0;32m"
CLEAR="\e[0m"

function help {
  echo "curve tool"
  echo ""
  echo "  usage: tool <command>"
  echo ""
  echo "  available commands:"
  echo "    run   - run the game"
  echo "    build - build the game for this platform"
  echo "    setup - setup virtualenv and install dependencies"
  echo "    test  - run unit tests"
  echo "    lint  - lint the code"
  echo "    clean - clean up all temporary files"
  echo "    help  - show this help"
}

case "$1" in
("run")
  ${ABSOLUTE_PATH}/bin/python3 ${ABSOLUTE_PATH}/src/main.py
  ;;

("build")
  ${ABSOLUTE_PATH}/bin/python3 -OO -m PyInstaller \
  ${ABSOLUTE_PATH}/src/main.py \
  --name="curve" \
  --onefile \
  --windowed \
  --add-data="config/**:config/" \
  --add-data="audio/**:audio/" \
  --add-data="img/**:img/" \
  --add-data="fonts/Exo/*:fonts/Exo/" \
  --add-data="fonts/Muli/*:fonts/Muli/" \
  --icon=img/icon.ico \
  --workpath=${ABSOLUTE_PATH}/build \
  --distpath=${ABSOLUTE_PATH}/dist \
  --clean \
  --strip
  ;;

("setup")
  echo -e "${GREY}Checking for ${MAGENTA}python3${CLEAR}..."
  command -v python3 --version >/dev/null 2>&1 || {
    echo -e >&2 "${RED}Could not find python3. Please install it and check if it is included in your path.${CLEAR}"
    exit 1
  }
  echo -e "${GREEN}Found python3${CLEAR}"

  echo -e "${GREY}Checking for ${MAGENTA}pip3${CLEAR}..."
  command -v pip3 --version >/dev/null 2>&1 || {
    echo -e >&2 "${RED}Could not find pip3. Please install it and check if it is included in your path.${CLEAR}"
    exit 1
  }
  echo -e "${GREEN}Found pip3${CLEAR}"
  
  echo -e "${GREY}Checking for ${MAGENTA}virtualenv${CLEAR}..."
  command -v virtualenv --version >/dev/null 2>&1 || {
    echo -e >&2 "${RED}Could not find virtualenv. Please install it and check if it is included in your path.${CLEAR}"
    exit 1
  }
  echo -e "${GREEN}Found virtualenv${CLEAR}"

  if [ ! -d ${ABSOLUTE_PATH}/bin ]; then
    echo -e "${GREY}Installing virtualenv...${CLEAR}"
    virtualenv -p python3 .
    echo -e "${GREEN}Installed virtualenv!${CLEAR}"
  fi
  echo -e "${GREY}virtualenv already installed.${CLEAR}"

  echo -e "${GREY}Installing dependencies...${CLEAR}"
  ${ABSOLUTE_PATH}/bin/pip3 install -r ${ABSOLUTE_PATH}/requirements.txt
  echo -e "${GREEN}Installed dependencies!${CLEAR}"

  ;;

("test")
  ${ABSOLUTE_PATH}/bin/python3 -m unittest discover -s ${ABSOLUTE_PATH}/test -p "*_test.py"
  ;;

("lint")
  ${ABSOLUTE_PATH}/bin/python3 -m pylint ${ABSOLUTE_PATH}/src/*.py
  ;;

("clean")
  rm -rf ${ABSOLUTE_PATH}/dist
  rm -rf ${ABSOLUTE_PATH}/build
  rm -rf ${ABSOLUTE_PATH}/**/__pychache__ # TODO: not working
  rm -f ${ABSOLUTE_PATH}/**.pyc
  rm -f ${ABSOLUTE_PATH}/*.spec
  rm -rf ${ABSOLUTE_PATH}/bin
  rm -rf ${ABSOLUTE_PATH}/lib
  rm -rf ${ABSOLUTE_PATH}/lib64
  rm -rf ${ABSOLUTE_PATH}/incldude
  rm -f ${ABSOLUTE_PATH}/pip-selfcheck.json
  ;;

("help")
  help
  ;;

*)
  help
  ;;
esac
