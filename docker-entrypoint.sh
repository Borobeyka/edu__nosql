#!/bin/sh

set -e

if [ "$1" = 'pgpool' ]; then

  configure-pgpool2

  sed -i "s:socket_dir = '.*':socket_dir = '/var/run/pgpool':g" /etc/pgpool2/pgpool.conf
  sed -i "s:pcp_socket_dir = '.*':pcp_socket_dir = '/var/run/pgpool':g" /etc/pgpool2/pgpool.conf
  IP_ADDR=$(ip addr show eth0 | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | head -1)
  sed -i "s:listen_addresses = '.*':listen_addresses = '$IP_ADDR':g" /etc/pgpool2/pgpool.conf

  gosu postgres "$@"
  
fi

exec "$@"