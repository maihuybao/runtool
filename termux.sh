# cd /sdcard
# pkg install python -y
output=$(python --version)
if [[ $output = 'Python 3.10.0' ]]
then
  python tool310.py
else
  python tool38.py
fi