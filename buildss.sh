git clone https://github.com/shadowsocks/shadowsocks-libev.git
cd shadowsocks-libev
mkdir -p ~/build-area/
cp ./scripts/build_deb.sh ~/build-area/
cd ~/build-area
./build_deb.sh
