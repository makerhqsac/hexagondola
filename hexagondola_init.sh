#!/bin/bash

### BEGIN INIT INFO
# Provides:          hexagondola
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: hexagondola
# Description:       hexagondola control and camera
### END INIT INFO
#
# /etc/init.d/hexagondola
# Subsystem file for "Hexagondola" server
#
# chkconfig: 2345 95 05 (1)
# description: Hexagondola server daemon
#
# processname: Hexagondola
# pidfile: /var/run/hexagondola.pid


RETVAL=0
prog="hexagondola"

start() {
        echo -n $"Starting $prog:"
        /usr/bin/python /root/hexagondola/app.py &> /dev/null &
        RETVAL=$?
        [ "$RETVAL" = 0 ] && echo $! > /var/run/hexagondola.pid
        echo
}

stop() {        
        echo  $"Stopping $prog:"
        if [ -e /var/run/hexagondola.pid ] 
        then
                hex_pid=`cat /var/run/hexagondola.pid`
                kill $hex_pid
                RETVAL=$?
        else
                echo "No pidfile. Is hexagondola running?"
                RETVAL=1
        fi
        [ "$RETVAL" = 0 ] && rm -f /var/run/hexagondola.pid
}

reload() {      
        echo -n $"Reloading $prog:"
        if [ -e /var/run/hexagondola.pid ] 
        then
                hex_pid=`cat /var/run/hexagondola.pid`
                kill $hex_pid -HUP
                RETVAL=$?
        else
                echo "No pidfile. Is hexagondola running?"
                RETVAL=1
        fi
        echo
}

status() {
        if [ -e /var/run/hexagondola.pid ] 
        then
                hex_pid=`cat /var/run/hexagondola.pid`
                echo "Hexagondola running as PID $hex_pid ." 
                RETVAL=$?
        else
                echo "Hexagondola not running."
                RETVAL=1
        fi

}

case "$1" in    
        start)
                start
                ;;
        stop)
                stop
                ;;
        restart)
                stop
                start
                ;;
        reload)
                reload
                ;;
        condrestart)
                if [ -f /var/run/hexagondola.pid ] ; then
                        stop
                        # avoid race
                        sleep 3
                        start
                fi
                ;;
        status)
                status 
                RETVAL=$?
                ;;
        *)      
                echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
                RETVAL=1
esac
exit $RETVAL

