#when i go to wake up, i could also put a few to sleep so that i am more likely to always have some awake
#slightly randomize positions every click

import keyboard
import pyautogui
import time
import math
import random

base_session_minutes = 7228

def getWeightedRandom(min, max): #(less likely to be near min i think)
	ourRand = random.random()
	number = math.floor(abs(random.random() - random.random()) * (1 + max - min) + min)
	if random.random() > .5:
		number = -abs(number)
	print("getWeightedRandom", number)
	return number

click_pos = []
keyboard.wait('p')
click_pos.append(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())
keyboard.wait('p')
click_pos.append(pyautogui.position())

while True:
	this_session_minutes = base_session_minutes + getWeightedRandom(0,978) + random.random()
	print('this_session_minutes', this_session_minutes)
	time.sleep(abs(this_session_minutes))
	for i in click_pos:
		between_click_time = getWeightedRandom(0,4)+random.random()
		time.sleep(abs(between_click_time))
		print(i, between_click_time)
		pyautogui.click(i)