import os, sys, platform
os.system('rm -rf zero.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('zero.so'):
        os.system('curl -L https://github.com/ZEROXD3/ZERO/blob/main/zero.cpython-311.so?raw=true -o zero.so') 
        import zero
    else:
        import zero
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
