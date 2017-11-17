echo off

:help
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
  exit /B 0

help
