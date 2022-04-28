pkg upgrade -y
pkg install python -y
curl https://raw.githubusercontent.com/maihuybao/runtool/rpwliker/rpwliker -o rpwliker
chmox 777 rpwliker
echo 'Cài đặt thành công, gõ ./rpwliker để vào tool'