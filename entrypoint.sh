#!/usr/bin/env bash

function web {
	echo "
	------------------
	Starting WebApp
	------------------
	"
	USER=`whoami`
	PID_FILE="/app/gunicorn/var/run/server.pid"
	gunicorn manage:app -c config/gunicorn_conf.py --capture-output --pid ${PID_FILE}
	echo "gunicorn started"

}

function update {
	echo "
	--------------------------
	Updating database ...
	--------------------------
	"
	python manage.py db upgrade
}

function bash {
	echo "
	------------------------
	Starting bash....
	------------------------
	"
	/bin/bash
}

case "$1" in 
  "web")
  web
  ;;

  "update")
  update
  ;;

  "bash")
  bash
  ;;
  *)

  echo "
  ---------------------------
  Usage: command [ARG]
   [ARG]:
   - 'web' for starting webapp with gunicorn
   - 'update' for updating the database
   - 'bash' to start a bash
 --------------------------------"
  exit 0
  ;;
esac  
 
  

