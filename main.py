#currently buggy, clean prints and make them very specific and debug
#we need a way to cancel, maybe unhook the listener when we are in the sequence loop

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

def write_to_file(click_pos_before, click_pos_mid, click_pos_after):
	print("write to file", click_pos_before)
	with open('click_pos_before.txt', 'w') as filehandle:
		for listitem in click_pos_before:
			filehandle.write('%s\n' % str(listitem))
	with open('click_pos_mid0.txt', 'w') as filehandle:
		for listitem in click_pos_mid[0]:
			filehandle.write('%s\n' % str(listitem))
	with open('click_pos_mid1.txt', 'w') as filehandle:
		for listitem in click_pos_mid[1]:
			filehandle.write('%s\n' % str(listitem))
	with open('click_pos_mid2.txt', 'w') as filehandle:
		for listitem in click_pos_mid[2]:
			filehandle.write('%s\n' % str(listitem))			
	with open('click_pos_after.txt', 'w') as filehandle:
		for listitem in click_pos_after:
			filehandle.write('%s\n' % str(listitem))
	print("write to file", click_pos_before, click_pos_mid, click_pos_after)

def read_from_file():
	print("read to file1",click_pos_before)
	click_pos_before_loaded = []
	with open('click_pos_before.txt', 'r') as filehandle:
		for line in filehandle:
			currentPlace = line[:-1]
			#print('currentPlace', currentPlace)
			coords = re.findall(r'\d+', currentPlace)
			#print('coords', coords)
			if len(coords) > 1:					
				class myPoint(object):
					pass
				mp = myPoint()
				mp.x = int(coords[0])
				mp.y = int(coords[1])
				click_pos_before_loaded.append(mp)
	click_pos_mid_load0 = []
	with open('click_pos_mid0.txt', 'r') as filehandle:
		for line in filehandle:
			currentPlace = line[:-1]
			#print('currentPlace', currentPlace)
			coords = re.findall(r'\d+', currentPlace)
			#print('coords', coords)
			if len(coords) > 1:					
				class myPoint(object):
					pass
				mp = myPoint()
				mp.x = int(coords[0])
				mp.y = int(coords[1])
				click_pos_mid_load0.append(mp)
	click_pos_mid_load1 = []
	with open('click_pos_mid1.txt', 'r') as filehandle:
		for line in filehandle:
			currentPlace = line[:-1]
			#print('currentPlace', currentPlace)
			coords = re.findall(r'\d+', currentPlace)
			#print('coords', coords)
			if len(coords) > 1:					
				class myPoint(object):
					pass
				mp = myPoint()
				mp.x = int(coords[0])
				mp.y = int(coords[1])
				click_pos_mid_load1.append(mp)
	click_pos_mid_load2 = []
	with open('click_pos_mid2.txt', 'r') as filehandle:
		for line in filehandle:
			currentPlace = line[:-1]
			#print('currentPlace', currentPlace)
			coords = re.findall(r'\d+', currentPlace)
			#print('coords', coords)
			if len(coords) > 1:					
				class myPoint(object):
					pass
				mp = myPoint()
				mp.x = int(coords[0])
				mp.y = int(coords[1])
				click_pos_mid_load2.append(mp)
	click_pos_after_loaded = []
	with open('click_pos_after.txt', 'r') as filehandle:
		for line in filehandle:
			currentPlace = line[:-1]
			#print('currentPlace', currentPlace)
			coords = re.findall(r'\d+', currentPlace)
			#print('coords', coords)
			if len(coords) > 1:					
				class myPoint(object):
					pass
				mp = myPoint()
				mp.x = int(coords[0])
				mp.y = int(coords[1])
				click_pos_after_loaded.append(mp)
			print(click_pos_after_loaded)			
	print("read to file2",click_pos_before)
	return click_pos_before_loaded, click_pos_mid_load0, click_pos_mid_load1, click_pos_mid_load2, click_pos_after_loaded
#make work overnight:::
#occasionally click back button and then return to game

#make it use bottom more
#more set of fewer heros

#better consolidated:::
#make the motions that are 
#move & drag
# click_pos_mid_drag
# click_pos_mid_clicks
#click 1,2,3,4,5 position

base_session_minutes = 60
inProgrammingMode = True
current_sequence_number = 0

click_pos_before = []
click_pos_mid = [[] for i in range(3)]

click_pos_after = []
def sequence_loop():
	global current_sequence_number
	while True:
		print('click_pos_mid', click_pos_mid)
		this_session_minutes = base_session_minutes + getWeightedRandom(0,1)
		print('this_session_minutes', this_session_minutes, click_pos_before)
		# if current_sequence_number == 0:
		# 	current_sequence_number = 1
		for i in range(int(this_session_minutes),0,-1): #this is the terminal countdown
			sys.stdout.write(str(i)+' ')
			sys.stdout.flush()
			time.sleep(1)
		print("current_sequence_number: ", current_sequence_number)
		for pos in click_pos_before:
			print("aclick", pos)
			between_click_time = getWeightedRandom(2,4)
			time.sleep(abs(between_click_time))
			print(pos.x, between_click_time)
			pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
			time.sleep(.5)
		for idx, pos in enumerate(click_pos_mid[current_sequence_number]): #this should be able to iterate through list items and have their index
			print('click_pos_mid[current_sequence_number]', click_pos_mid[current_sequence_number])
			print('pos, idx', pos, idx)
			print("2current_sequence_number: ", current_sequence_number)

			should_do = "click"
			if current_sequence_number*4 > idx:
				if (idx % 2) == 0 or idx == 0:
				   should_do = "move"
				else:
				   should_do = "drag"


			if should_do == "click":
				between_click_time = getWeightedRandom(2,4)
				time.sleep(abs(between_click_time))
				print(pos.x, between_click_time)
				time.sleep(.2)
				pyautogui.click(pos.x+getWeightedRandom(1,4), pos.y+getWeightedRandom(1,4))
				time.sleep(.2)
				#pyautogui.click(pos.x+getWeightedRandom(1,4), pos.y+getWeightedRandom(1,4))

			if should_do == "move":
				pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2))
				print('2move to ', pyautogui.position())
				time.sleep(.5)
				pyautogui.mouseDown(button='left')				

			if should_do == "drag":
				print("3drag to ", pyautogui.position())
				pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2), duration=getWeightedRandom(2,5))	
				time.sleep(.5)
				pyautogui.mouseUp(button='left')

			# 	if idx == 0:
			# 		pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2))
			# 		time.sleep(.5)
			# 		pyautogui.mouseDown(button='left')
			# 		print('0move to ', pyautogui.position())
			# 	elif idx == 1:
			# 		pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2), duration=getWeightedRandom(2,5))
			# 		time.sleep(.5)
			# 		pyautogui.mouseUp(button='left')
			# 		print("1drag to ", pyautogui.position())
			# 	elif current_sequence_number == 2 and idx == 2:
			# 		pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2))
			# 		print('2move to ', pyautogui.position())
			# 		time.sleep(.5)
			# 		pyautogui.mouseDown(button='left')
			# 	elif current_sequence_number == 2 and idx == 3:
			# 		print("3drag to ", pyautogui.position())
			# 		pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2), duration=getWeightedRandom(2,5))	
			# 		time.sleep(.5)
			# 		pyautogui.mouseUp(button='left')			
			# 	elif current_sequence_number == 2 and idx == 4:
			# 		pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2))
			# 		print('2move to ', pyautogui.position())
			# 		time.sleep(.5)
			# 		pyautogui.mouseDown(button='left')
			# 	elif current_sequence_number == 2 and idx == 5:
			# 		print("3drag to ", pyautogui.position())
			# 		pyautogui.moveTo(pos.x+getWeightedRandom(0,2), pos.y+getWeightedRandom(0,2), duration=getWeightedRandom(2,5))	
			# 		time.sleep(.5)
			# 		pyautogui.mouseUp(button='left')	
			# 	else:
			# 		print(pos.x, between_click_time)
			# 		pyautogui.click(pos.x+getWeightedRandom(1,4), pos.y+getWeightedRandom(1,4))
			# 		time.sleep(.2)
			# 		pyautogui.click(pos.x+getWeightedRandom(1,4), pos.y+getWeightedRandom(1,4))
			# else:
			# 	between_click_time = getWeightedRandom(1,3)
			# 	time.sleep(abs(between_click_time))
			# 	pyautogui.click(pos.x+getWeightedRandom(1,4), pos.y+getWeightedRandom(1,4))
			# 	time.sleep(.2)
			# 	pyautogui.click(pos.x+getWeightedRandom(1,4), pos.y+getWeightedRandom(1,4))
		for pos in click_pos_after:
			print('click_pos_after', pos)
			between_click_time = getWeightedRandom(1,3)
			print('after between_click_time', between_click_time)
			time.sleep(abs(between_click_time))
			print(pos.x, between_click_time)
			pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
			time.sleep(.2)
			pyautogui.click(pos.x+getWeightedRandom(0,6), pos.y+getWeightedRandom(0,6))
			time.sleep(.5)
		current_sequence_number = current_sequence_number + 1
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
			click_pos_before.append(pyautogui.position())
			print('a ', pyautogui.position())
		if key.char == ('1'):
			print('1 ', pyautogui.position())
			click_pos_mid[0].append(pyautogui.position())
			print('click_pos_mid', click_pos_mid)
		if key.char == ('2'):
			print('2 ', pyautogui.position())
			click_pos_mid[1].append(pyautogui.position())
		if key.char == ('3'):
			print('3 ', pyautogui.position())
			click_pos_mid[2].append(pyautogui.position())
		if key.char == ('s'):
			print('s ', pyautogui.position())
			click_pos_after.append(pyautogui.position())
		if key.char == ('d'):
			print('d sequenceloop()')
			#inProgrammingMode = False
			sequence_loop()
		if key.char == ('w'):
			print('w pressed')
			write_to_file(click_pos_before, click_pos_mid, click_pos_after)
		if key.char == ('r'):
			print('r pressed')
			click_pos_before, click_pos_mid0, click_pos_mid1, click_pos_mid2, click_pos_after = read_from_file()
			click_pos_mid = [click_pos_mid0, click_pos_mid1, click_pos_mid2]
			print("read to file3",click_pos_before)
		if key.char == ('q'):
			print('quit')
			sys.exit()
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
