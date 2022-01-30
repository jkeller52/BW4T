import pyautogui
import os

screenWidth, screenHeight = pyautogui.size()
#print(screenWidth, screenHeight)

#User sets map upon program start --> can change later (need function/button to do so)
Map = input("Enter the map code (Ex: Pilot1")
roomNumber = input("Enter the Room Letter and Number (ex: A2):")



#example test to pass a1 into pyautogui.rightClick
A1 = (x=150, y=1200)

dropzoneX, dropzoneY



def go_to_room(roomNumber):
#right click over target room
	pyautogui.rightClick(x=moveToX, y=moveToY)
	pyautogui.PAUSE(.001)
#left click "Go to RoomX#" 
	pyautogui.click(x=moveToX, y=moveToY, clicks=1, interval=secs_between_clicks, button='left')
	pyautogui.PAUSE(.001)

def go_to_dropzone():
#scroll and right click over "drop zone"
	pyautogui.rightClick(x=moveToX, y=moveToY)
	pyautogui.PAUSE(.001)
	#left click go to DropZone
	pyautogui.click(x=moveToX, y=moveToY, clicks=1, interval=secs_between_clicks, button='left')



def comms_block_dropped_off():
#
	pyautogui.click(x=moveToX, y=moveToY, clicks=1, interval=secs_between_clicks, button='right')
	pyautogui.PAUSE(.001)
	pyautogui.click(x=moveToX, y=moveToY, clicks=1, interval=secs_between_clicks, button='left')



while


###Inputs will help create a system where the researcher can use the tool dynamically
print()


###MAP Logic
if Map == Pilot1:
	with open("BW4T/BW4T-Clicker/Pilot1.csv") as file:




###Problems 
# Have to set coords for position of rooms, drop zone on each map
#variables might make this easier: var Map#Room# = (x,y) or var Map#Dropzone = (x,y)
#something to remember - server needs restarted between runs
#setting variables dynamically will make this harder, but be worth it in the end bc of the need to switch maps



