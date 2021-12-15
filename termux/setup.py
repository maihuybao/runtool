import platform,os
type = platform.machine()
if type == 'arm' or type == 'armv8l':
  os.system('curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/command/arm.sh | bash')
if type == 'arm64':
  os.system('curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/command/arm64.sh | bash')
if type == 'aarch64':
  os.system('curl https://raw.githubusercontent.com/maihuybao/runtool/main/termux/command/aarch64.sh | bash ')