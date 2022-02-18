#detect first X keypress positions
#pick random amount of minutes around 120
#	use this number to set the amount of time for the first click
#	give all other times a random small amount after that and then for each of the rest
#do the mouse clicks at their times
#then go back to 2

import math
import random
import pyxhook

def getWeighterRandom(min, max):
	ourRand = random.random()
	number = math.floor(abs(random.random() - random.random()) * (1 + max - min) + min)
	print(number)

import pyautogui
position = pyautogui.locateCenterOnScreen('image.png')
print(position.x/2,position.y/2)
pyautogui.click(position.x/2,position.y/2)

getWeighterRandom(0, 3000)

#todo
#take screenshot(or use one took) and make image.png with small item