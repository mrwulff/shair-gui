sudo apt-get install swig scons build-essential git autoconf automake libtool libdaemon-dev libasound2-dev libpopt-dev libconfig-dev avahi-daemon libavahi-client-dev libssl-dev xbindkeys xbindkeys-config
pip install pygame obd

git clone https://github.com/jgarff/rpi_ws281x/tree/master/python
git clone https://github.com/thilaire/rpi-TM1638.git




git clone https://github.com/mikebrady/shairport-sync.git  
cd shairport-sync  
autoreconf -i -f  

 ./configure --sysconfdir=/etc --with-alsa --with-avahi --with-ssl=openssl --with-metadata --with-systemd --with-apple
make  

getent group shairport-sync &>/dev/null || sudo groupadd -r shairport-sync >/dev/null  
getent passwd shairport-sync &> /dev/null || sudo useradd -r -M -g shairport-sync -s /usr/bin/nologin -G audio shairport-sync >/dev/null  

sudo make install  
sudo systemctl enable shairport-sync 
