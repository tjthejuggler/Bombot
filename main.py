#detect first X keypress positions
#pick random amount of minutes around 120
#	use this number to set the amount of time for the first click
#	give all other times a random small amount after that and then for each of the rest
#do the mouse clicks at their times
#then go back to 2


#between wakeups, do in/out of game clicks to prevent timeout

import keyboard

import pyautogui
import time
import math
import random


def getWeightedRandom(min, max): #(less likely to be near min i think)
	ourRand = random.random()
	number = math.floor(abs(random.random() - random.random()) * (1 + max - min) + min)
	if random.random() > .5:
		number = -abs(number)
	print("getWeightedRandom", number)
	return number

base_session_minutes = 7228

getWeightedRandom(0, 3000)


click_pos = []
keyboard.wait('p')
click_pos.append(pyautogui.position())
print(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
print(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
pyautogui.click(20, 100)

# pyautogui.moveRel(0, 10) 

while True:
	this_session_minutes = base_session_minutes + getWeightedRandom(0,978) + random.random()
	print('this_session_minutes', this_session_minutes)
	time.sleep(abs(this_session_minutes))
	for i in click_pos:
		between_click_time = getWeightedRandom(0,4)+random.random()
		time.sleep(abs(between_click_time))
		print(i, between_click_time)
		pyautogui.click(i)
		

#todo
#take screenshot(or use one took) and make image.png with small item