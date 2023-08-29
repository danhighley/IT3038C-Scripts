#!/bin/bash

# This script ouputs the IP address and Hostname of a machine
greeting="This is a script. Hello!"
echo "$greeting, thanks for joining us!"
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME
a=$(ip a | grep 'noprefixroute dynamic ens192' | awk '{print $2}')
echo My IP is $a
