#!/bin/sh

case "$1" in
("run")
  . scripts/unix/game.sh
  ;;

("run_server")
  cd server && cargo run
  ;;

("build")
  . scripts/unix/build.sh
  ;;

("build_server")
  cd server && cargo build --release
  ;;

("setup")
  . scripts/unix/setup.sh
  ;;

("setup_dev")
  . scripts/unix/setup_dev.sh
  ;;

("test")
  . scripts/unix/test.sh
  ;;

("lint")
  . scripts/unix/lint.sh
  ;;

("help")
  . scripts/unix/help.sh
  ;;

*)
  . scripts/unix/help.sh
  ;;
esac
