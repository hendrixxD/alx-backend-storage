#!/bin/bash

sudo su root

mkdir -p /etc/redis/

touch /etc/redis/6379.conf

vim /etc/redis/6379.conf

# paste the following below 

# port              6379
# daemonize         yes
# save              60 1
# bind              127.0.0.1
# tcp-keepalive     300
# dbfilename        dump.rdb
# dir               ./
# rdbcompression    yes
