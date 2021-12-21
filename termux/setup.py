import platform,os
type = platform.machine()
print('\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mTiến Hành Cài Đặt \033[1;32mPython, Curl \033[1;37m...')
os.system('pkg install python curl -y')
print('\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mTiến Hành Cài Đặt \033[1;32mThư Viện Python \033[1;37m...')
os.system('pip install requests uuid')
print('\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mĐang Tìm Phiên Bản \033[1;32mThích Hợp \033[1;37m...')
print('\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mTiến Hành Cài Đặt \033[1;32mGói Tool \033[1;37m...')
if type == 'arm' or type == 'armv8l' or type == 'armv7l':
  print(f'\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mĐã Tìm Thấy Phiên Bản \033[1;32m{type} \033[1;37m Phù Hợp Với Thiết Bị Của Bạn...')
  os.system('curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/command/arm.sh | bash')
if type == 'arm64':
  print(f'\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mĐã Tìm Thấy Phiên Bản \033[1;32m{type} \033[1;37m Phù Hợp Với Thiết Bị Của Bạn...')
  os.system('curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/command/arm64.sh | bash')
if type == 'aarch64':
  print(f'\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mĐã Tìm Thấy Phiên Bản \033[1;32m{type} \033[1;37m Phù Hợp Với Thiết Bị Của Bạn...')
  os.system('curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/command/aarch64.sh | bash ')
else:
  print(f'\033[1;37m[\033[1;31m!\033[1;37m] \033[1;37mKhông Thể Tìm Thấy Phiên Bản \033[1;32m{type}\033[1;37m Phù Hợp Với Thiết Bị Của Bạn ...')
