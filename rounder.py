import math
def rounder(num, base, direction):
	if direction == "down":
		val = int(base * math.floor(float(num)/base))
	elif direction == "up":
		val = int(base * math.ceil(float(num)/base))
	return val
