sudo chmod a+rw /dev/ttyUSB0
wget http://192.168.100.1:8080/?action=snapshot -O chk.jpg
eog chk.jpg
rm chk.jpg
