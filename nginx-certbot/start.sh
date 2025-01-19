#!/bin/bash
nginx -g "daemon off;" &
nginx_pid=$!
sleep 5  # Wait for Nginx to start
certbot --nginx --quiet --no-self-upgrade
wait $nginx_pid