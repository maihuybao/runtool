curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/deb/maihuybao_arm64.deb -o maihuybao.deb
dpkg -i maihuybao.deb
cd ${PREFIX}
chmod +x maihuybao