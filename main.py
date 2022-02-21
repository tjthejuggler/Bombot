#when i go to wake up, i could also put a few to sleep so that i am more likely to always have some awake
#slightly randomize positions every click

#try running this with half the heros sleeping all the time. Do this once we have a bunch of full health


import keyboard
import pyautogui
import time
import math
import random
import sys

def getWeightedRandom(min, max): #(less likely to be near min i think)
	ourRand = random.random()
	number = math.floor(abs(random.random() - random.random()) * (1 + max - min) + min)
	if random.random() > .5:
		number = -abs(number)
	print("getWeightedRandom", number)
	return number + random.random()

base_session_minutes = 828
inProgrammingMode = True
current_sequence_number = 0

click_pos_before = []
click_pos_1 = []
click_pos_2 = []
click_pos_3 = []
click_pos_after = []

while inProgrammingMode:
	print('inProg')
	if keyboard.read_key() == "a":
		click_pos_before.append(pyautogui.position())
	# if keyboard.read_key() == "1":
	# 	click_pos_.mid[0].append(pyautogui.position())		
	# if keyboard.read_key() == "2":
	# 	click_pos_.mid[1].append(pyautogui.position())
	# if keyboard.read_key() == "3":
	# 	click_pos_.mid[2].append(pyautogui.position())
	# if keyboard.read_key() == "s":
	# 	click_pos_after.append(pyautogui.position())
	if keyboard.read_key() == "d":
		print('d pressed')
		inProgrammingMode = False

		
while not inProgrammingMode:
	this_session_minutes = base_session_minutes + getWeightedRandom(0,321)
	print('this_session_minutes', this_session_minutes, click_pos_before)

	for i in range(int(this_session_minutes),0,-1):
	    sys.stdout.write(str(i)+' ')
	    sys.stdout.flush()
	    time.sleep(1)
	#time.sleep(this_session_minutes)
	for pos in click_pos_before:
		print(pos)
		between_click_time = getWeightedRandom(0,4)
		time.sleep(abs(between_click_time))
		print(pos.x, between_click_time)
		pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
	for idx, pos in enumerate(click_pos_mid[current_sequence_number]): #this should be able to iterate through list items and have their index
		between_click_time = getWeightedRandom(0,4)
		time.sleep(abs(between_click_time))
		if idx == 0:
			pyautogui.moveTo(pos.x+getWeightedRandom(0,4), pos.y+getWeightedRandom(0,4))
		elif idx == 1:
			pyautogui.dragTo(pos.x+getWeightedRandom(0,4), pos.y+getWeightedRandom(0,4), button='left')
		else:
			#do drag stuff(no need to do it if we are on the 0th sequence)
			print(click_pos)
			print(pos.x, between_click_time)
			pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
	for pos in click_pos_after:
		print('click_pos_after', pos)
		between_click_time = getWeightedRandom(0,4)
		time.sleep(abs(between_click_time))
		print(pos.x, between_click_time)
		pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
	current_sequence_number =+ 1
	if current_sequence_number == 3:
		current_sequence_number = 0

		




#make it save training to a txt file by default and use this training by default if training is skipped
#	make a key that specifically goes into retraining mode

#make a key that is "force next sequence"
#make a key that is "toggle training/doing"

#visible countdown timer to next sequence

#movie gambling live during movies if there is always new releases
