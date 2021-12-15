echo "Tiến hành cài extension"
cp src.so /data/data/com.termux/files/usr/lib/tool.so
rm -rf src.so
echo "Tiến hành setup Termux"
pkg install python git -y
echo "Tiến hành vào tool"
python main.py
