#!/bin/sh

case "$1" in
("run")
  . scripts/unix/game.sh
  ;;

("build")
  . scripts/unix/build.sh
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
