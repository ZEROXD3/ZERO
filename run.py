import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
#os.system('xdg-open https://www.facebook.com/gsriyad11')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf zero.so')
except:
    pass
os.system('rm -rf zero.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('zero.so'):
        os.system('curl -L https://github.com/ZEROXD3/ZERO/blob/main/zero.so?raw=true -o zero.so') 
        import zero
    else:
        import zero
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
