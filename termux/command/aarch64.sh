curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/deb/maihuybao_aarch64.deb -o maihuybao.deb
dpkg -i maihuybao.deb
cd /data/data/com.termux/files/usr/bin/
chmod +x maihuybao
echo -e '\e[32mSetup Thành Công\e[0m'
echo -e '\e[33mGõ\e[0m: \e[35mmaihuybao\e[0m \e[33mđể vào tool\e[0m'