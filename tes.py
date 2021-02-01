import os
import subprocess
import getpass

wd = os.getcwd() + '/'
# os.chdir("~/")
# subprocess.run(['mkdir', 'cekGan'])

username = getpass.getuser()
homeDir = f'/home/{username}/'
os.chdir(homeDir+'.icons/')
# subprocess.run(['ls', '-a'])
subprocess.run(["echo"])
