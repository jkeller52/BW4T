import pyautogui
import os

#User sets map upon program start --> can change later (need function/button to do so)

#Need: position above info in function arguments!
#goal: main functions work for each map nav states.
#think about how wizard of oz will work... reading text commands from 

class mapNavigation:
	
	def go_to_dropzone(mapvar,destination):
		if mapvar == map4:
			dz = (1073, 110)
			goto_dz = (879,55)

		 	A1 = (609, 103)
		 	goto_A1 = (665, 67)

		 	A2 = (617,218)
			goto_A2 = (655,70)

			A5 = (619,544)
			goto_A5 = (627,95)

			C3 = (840, 325)
			goto_C3 = (825,80)

			C5 = (841,539)
		 	goto_C5 = (823,105)

		 	D3 = (960, 332)
			goto_D3 = (803, 79)

			E3 = (1071,339)
			goto_E3 = (755, 85)

			E5 = (1051,555)
			goto_E5 = (867,102)
			
		if destination == dz:
			pyautogui.rightClick(dz) 
			time.sleep(0.1)
			pyautogui.rightClick(goto_dz) 

		if destination == A1:
			pyautogui.rightClick(A1)
			time.sleep(0.1)
			pyautogui.rightClick(goto_A1)


		if destination == A:
			pyautogui.rightClick(A5)
			time.sleep(0.1)
			pyautogui.rightClick(goto_A5)



		# 	if destination == C5 
		# 		

			if destination == E5:	
				

				

				

		# 		

		# 		


		# 	else:
		# 		print("Error")
		# if mapvar == map5:

# 		pyautogui.rightClick(destination)
# 		time.sleep(0.1)
# 		pyautogui.leftClick(goto_dz)


# 	def go_to_room(room_coords,coords_goto_room):
# 		#room_coords= []
# 		#goto_room = []
# 		pyautogui.rightClick(coords_dz) #click "JacobMap6"
# 		time.sleep(0.1)
# 		pyautogui.leftClick(coords_goto_dz)


# #	pyautogui.clickRel() #NEED to create room nav variables to be RELATIVE to current position of mouse.

# 	def drop_block():
# 		print("yes")
	
# 	def pickup_block():
# 		print("yes")

# 	def robot_comms():
# 		print("yes")

go_to_dropzone(mapvar, destination)


#with open("/Users/Jacob/BW4T/maps/JacobMap4.map") as map4:



###Problems 
# Have to set coords for position of rooms, drop zone on each map
#variables might make this easier: var Map#Room# = (x,y) or var Map#Dropzone = (x,y)
#something to remember - server needs restarted between runs
#setting variables dynamically will make this harder, but be worth it in the end bc of the need to switch maps



