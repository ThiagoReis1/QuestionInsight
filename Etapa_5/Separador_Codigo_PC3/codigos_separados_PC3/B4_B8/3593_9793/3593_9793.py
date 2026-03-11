from numpy import *

dice = array(eval(input('SAQUI> ')))
point = 200
i = 0

while i < size(dice):
	if dice[i] == 1:
		point = point / 2
	elif dice[i] == 2:
		point = point * 3
	elif dice[i] == 3:
		point = point / 2
	elif dice[i] == 4:
		point = point * 3
	elif dice[i] == 5:
		point = point / 2
	elif dice [i] == 6:
		point = point * 3
	i = i + 1
		
print(round(point, 2))