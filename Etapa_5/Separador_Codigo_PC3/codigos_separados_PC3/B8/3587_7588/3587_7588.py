from numpy import *

h = array(eval(input()))

score = 100

i = 0


while(i < size(h)):
	if(h[i] == 1):
		score *= 5
	elif(h[i] == 2):
		score *= 3
	elif(h[i] == 3):
		score += 0
	elif(h[i]):
		score /= 2
	i += 1

print(round(score, 2))