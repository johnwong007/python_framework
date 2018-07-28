#!/bin/bash

RETVAL=0
prog="eas"
prog_python="python2.6"

echo '=====================eas.sh====================='
if [ "$PROG_PYTHON"='' ]
then
	export PROG_PYTHON=$(which $prog_python)
fi

prog_python=$PROG_PYTHON
prog_dir=$(cd $(dirname $0)/..; pwd)
prog_py="$prog_dir/bin/$0.py"
prog_pid="$prog_dir/var/run/$prog.$1.pid"
prog_loop="$prog_dir/var/run/$prog.$1.loop"
prog_output="$prog_dir/var/log/$prog.$1.output"

mkdir -p $(dirname $prog_pid)
mkdir -p $(dirname $prog_output)

# . /etc/rc.d/init.d/functions

# echo $(ls $(dirname "/etc/rc.d/init.d/functions"))

start()
{
	if [ -f "$prog_loop"]; then
		echo "prog_loop exists"
	fi
	echo "prog_loop not exists"
	return $RETVAL
}

start ;









echo '=====================eas.sh====================='

exit $RETVAL

