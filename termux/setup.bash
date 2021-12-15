echo "Tiến hành cài extension"
cp tool.so /data/data/com.termux/files/usr/lib/tool.so
echo "Tiến hành setup Termux"
pkg install python git -y
echo "Tiến hành vào tool"
python tool.py