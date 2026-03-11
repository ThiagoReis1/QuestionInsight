import math

def h(x):
	if x <= -1 or x >= 1:
		print(round(abs(x**(1/2)),2))
	elif x == 0.0:
		print(0)
	else:
		print(round(abs(x),2))
		
h(float(input()))
		