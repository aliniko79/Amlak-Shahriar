#!/bin/bash
certbot renew --quiet --no-self-upgrade
nginx -s reload