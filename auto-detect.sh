#!/bin/bash

echo "stop bluetooth"
sudo service bluetooth stop
ls /dev/input/* > pre
sudo service bluetooth start
echo "CONNECT your BT button"
echo "Press any key to continue"
read
ls /dev/input/* > post
new_devices=$(diff --unchanged-line-format='' --new-line-format='%L' post pre)

for i in $new_devices
do
    echo "chmod ${i} to 666"
    sudo chmod 666 $i
done

python3 mute.py
