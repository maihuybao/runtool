pkg upgrade -y
pkg install python curl -y
curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/motd -o ${PREFIX}/etc/motd
curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/setup.py | python