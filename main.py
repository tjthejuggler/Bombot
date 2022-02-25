#currently buggy, clean prints and make them very specific and debug
#we need a way to cancel, maybe unhoiok the listener when we are in the sequence loop


# options
# continue trying to hook up to the newest block
# look for a transaction to a specific address and do something like this
#       Just switch the bitcoin address in the url below to your bitcoin address, and import the json into a webapp. https://blockchain.info/address/$bitcoin_address?format=json
# look into verifying signed messages (as first step verifying that a particular address has a specific nft)

#when get signed message, get that address
#       
#be able to a qr on phone that proves ownership of address
#       read the qr code on computer
#       check the address of the signed message
#       look for transactions in that address
#       look for all UTXOs in that address and see if any are our "colored coin"

import keyboard
import pyautogui
import time
import math
import random
import sys
import re
from shapely.geometry import Point
from pynput.keyboard import Key, Listener

def getWeightedRandom(min, max): #(less likely to be near min i think)
	ourRand = random.random()
	number = math.floor(abs(random.random() - random.random()) * (1 + max - min) + min)
	if random.random() > .5:
		number = -abs(number)
	print("getWeightedRandom", number)
	return number + random.random()

def write_to_file(click_pos_before):
	print("write to file", click_pos_before)
	with open('click_pos_before.txt', 'w') as filehandle:
		for listitem in click_pos_before:
			filehandle.write('%s\n' % str(listitem))
	print("write to file", click_pos_before)

def read_from_file():
	print("read to file1",click_pos_before)
	click_pos_before_loaded = []
	with open('click_pos_before.txt', 'r') as filehandle:
		for line in filehandle:
			currentPlace = line[:-1]
			print('currentPlace', currentPlace)
			coords = re.findall(r'\d+', currentPlace)
			print('coords', coords)
			if len(coords) > 1:					
				class myPoint(object):
				    pass
				mp = myPoint()
				mp.x = int(coords[0])
				mp.y = int(coords[1])
				click_pos_before_loaded.append(mp)
			print(click_pos_before_loaded)
	print("read to file2",click_pos_before)
	return click_pos_before_loaded

base_session_minutes = 10
inProgrammingMode = True
current_sequence_number = 0

click_pos_before = []
click_pos_mid = [[]]*3
click_pos_after = []
def sequence_loop():
	global current_sequence_number
	while True:
		this_session_minutes = base_session_minutes + getWeightedRandom(0,1)
		print('this_session_minutes', this_session_minutes, click_pos_before)
		for i in range(int(this_session_minutes),0,-1):
			sys.stdout.write(str(i)+' ')
			sys.stdout.flush()
			time.sleep(1)
		for pos in click_pos_before:
			print(pos)
			between_click_time = getWeightedRandom(0,4)
			time.sleep(abs(between_click_time))
			print(pos.x, between_click_time)
			pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
		for idx, pos in enumerate(click_pos_mid[current_sequence_number]): #this should be able to iterate through list items and have their index
			between_click_time = getWeightedRandom(0,4)
			time.sleep(abs(between_click_time))
			if current_sequence_number > 0:
				if idx == 0:
					pyautogui.moveTo(pos.x+getWeightedRandom(0,4), pos.y+getWeightedRandom(0,4))
				elif idx == 1:
					pyautogui.dragTo(pos.x+getWeightedRandom(0,4), pos.y+getWeightedRandom(0,4), button='left')
				elif current_sequence_number == 2 and idx == 2:
					pyautogui.moveTo(pos.x+getWeightedRandom(0,4), pos.y+getWeightedRandom(0,4))
				elif current_sequence_number == 2 and idx == 3:
					pyautogui.dragTo(pos.x+getWeightedRandom(0,4), pos.y+getWeightedRandom(0,4), button='left')				
				else:
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

def show(key):
	global click_pos_before
	global click_pos_mid
	global click_pos_after
	if key == Key.delete: 
		return False	
	if hasattr(key,'char'):
		if key.char == ('a'):
			print('new a')
			click_pos_before.append(pyautogui.position())
			print(click_pos_before) 	  
		if key.char == ('1'):
			click_pos_mid[0].append(pyautogui.position())
		if key.char == ('2'):
			click_pos_mid[1].append(pyautogui.position())
		if key.char == ('3'):
			click_pos_mid[2].append(pyautogui.position())
		if key.char == ('s'):
			click_pos_after.append(pyautogui.position())
		if key.char == ('d'):
			#inProgrammingMode = False
			sequence_loop()
		if key.char == ('w'):
			print('w pressed')
			write_to_file(click_pos_before)
		if key.char == ('r'):
			print('r pressed')
			click_pos_before = read_from_file()
			print("read to file3",click_pos_before)
# Collect all event until released
with Listener(on_press = show) as listener:
	listener.join()

# while inProgrammingMode:
# 	print('inProg')
# 	if keyboard.read_key() == "a":
# 		click_pos_before.append(pyautogui.position())
# 		print(click_pos_before)
# 	if keyboard.read_key() == "1":
# 		click_pos_mid[0].append(pyautogui.position())		
# 	if keyboard.read_key() == "2":
# 		click_pos_mid[1].append(pyautogui.position())
# 	if keyboard.read_key() == "3":
# 		click_pos_mid[2].append(pyautogui.position())
# 	if keyboard.read_key() == "s":
# 		click_pos_after.append(pyautogui.position())
# 	if keyboard.read_key() == "d":
# 		print('d pressed')
# 		inProgrammingMode = False
# 	if keyboard.read_key() == "w":
# 		print('w pressed')
# 		write_to_file(click_pos_before)
# 	if keyboard.read_key() == "r":
# 		print('r pressed')
# 		click_pos_before = read_from_file()


		




#make it save training to a txt file by default and use this training by default if training is skipped
#	make a key that specifically goes into retraining mode

#make a key that is "force next sequence"
#make a key that is "toggle training/doing"

#visible countdown timer to next sequence

#movie gambling live during movies if there is always new releases
