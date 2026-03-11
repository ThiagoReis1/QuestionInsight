from numpy import *
targeted = array(eval(input()))
i = 0
score = 0
while i != len(targeted):
	if targeted[i] == 1:
		score += 80
	elif targeted[i] == 2:
		score += 40
	elif targeted[i] == 3:
		score+= 20
	elif targeted[i] == 4:
		score+= 10
	i = i + 1
print(score)