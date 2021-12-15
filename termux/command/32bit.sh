curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/deb/maihuybao_arm.deb -o maihuybao.deb
dpkg -i maihuybao.deb
cd ${PREFIX}
chmod +x maihuybao