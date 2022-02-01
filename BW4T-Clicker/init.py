import pyautogui
import subprocess
import time


mapvar = []
Scenario5 = []


def main():
	
	#mapSelector()
	#time.sleep(4)
	startClient()
	startServer()
	#time.sleep(4)
	#resizeServerGUI()
	#time.sleep(1)
	#resizeClientGUI()

class start_applications:
#intializes server in new shell
	def startServer():
		try:
			output = subprocess.check_output(["open", "-F", "-a", "Terminal", '/Users/jacobkeller/BW4T/BW4T-Clicker/StartServer.sh'])
		except subprocess.CalledProcessError:
			if output:
				print(output)

	def startClient(): #might not need new terminal window
	# subprocess.call(['sh', '/Users/jacobkeller/BW4T/BW4T-Clicker/StartClient.sh'])
	#time.sleep(2)
		try:
			output = subprocess.check_output(["open", "-F", "-a", "Terminal", '/Users/jacobkeller/BW4T/BW4T-Clicker/StartClient.sh'])
		except subprocess.CalledProcessError:
			if output:
			print(output)


#resizes server GUI
def resizeServerGUI():
		#time.sleep(6)
		pyautogui.leftClick(x=18, y=380)
		pyautogui.hotkey('ctrl', 'option', "left")  #resizes selected window to left 1/3 of screen
		# ^, Option, Up Arrow, Left Arrow /// 
		time.sleep(.01)
		pyautogui.hotkey('ctrl', 'option', "shift", "left") #Makes screen smaller 3x
		pyautogui.hotkey('ctrl', 'option', "shift", "left")
		pyautogui.hotkey('ctrl', 'option', "shift", "left")
		###MAP Logic





def resizeClientGUI():
	#	time.sleep(2)
		#time.sleep(4)
		pyautogui.leftClick(843,45) #clicks the window
		time.sleep(0.1)
		pyautogui.hotkey('command', 'option', "right") #Makes client gui right half of display
		pyautogui.moveTo(840,993, duration=.5) #moves mouse to bottom left corner of client
		pyautogui.dragTo(567, 994, duration=.5, button='left') #drag bottom left corner of client to desired size


def mapSelector():
	startServer()
	time.sleep(8)
	#resizeServerGUI() /// don't need this here
	mapvar = input("Select a Map: ")
	if mapvar == "Map4":
		#Need a way to configure variables based on map choice
		time.sleep(.5)
		pyautogui.leftClick(205,62) #click "Change Map"
		time.sleep(.5)
		pyautogui.leftClick(185,64) #click "JacobMap4"
		time.sleep(1)
		startClient()
		resizeServerGUI() #resizes GUI
		time.sleep(3)
		resizeClientGUI()
	if mapvar == "Map5":
		pyautogui.leftClick(220,62) #click "Change Map"
		time.sleep(1)
		pyautogui.leftClick(190,97) #click "JacobMap5"
		time.sleep(1)
		startClient()
		resizeServerGUI() #resizes GUI
		time.sleep(3)
		resizeClientGUI()
	if mapvar == "Map6":
		pyautogui.leftClick(220,62) #click "Change Map"
		time.sleep(1)
		pyautogui.leftClick(155,150) #click "JacobMap6"
		startClient()
		time.sleep(1)
		resizeServerGUI() #resizes GUI
		time.sleep(3)
		resizeClientGUI()

	#		with open("BW4T/BW4T-Clicker/Pilot1.csv") as file:
	#		pyautogui.click(x=moveToX, y=moveToY, clicks=1, interval=secs_between_clicks, button='left')

#CALL FUNCTIONS: Starts server and client, sets their dimensions


main()



#Need a way to configure variables based on map choice

