import subprocess
import platform

win = platform.system() == "Windows"
#lin = platform.system() == "Linux"
icmp_out = subprocess.Popen('ipconfig' if win else 'ifconfig' ,shell=True,stdout=subprocess.PIPE)
#icmp_out = subprocess.Popen('ipconfig' if win else 'ifconfig' if lin else '' ,shell=True,stdout=subprocess.PIPE)
stdout, stderr = icmp_out.communicate(timeout=5)
print(stdout.decode(encoding=("gbk" if win else "utf8")))


print('***')