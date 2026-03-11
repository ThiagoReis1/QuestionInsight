from numpy import *
total = 100
dice = array(eval(input("insert the dices: ")),dtype=int)

for h in range(size(dice)):
	if(dice[h] == 6):
		total = total * 6
	elif(dice[h] == 5):
		total = total / 5
	elif(dice[h] == 4):
		total = total * 4
	elif(dice[h] == 3):
		total = total / 3
	elif(dice[h] == 2):
		total = total * 2
		
print(round(total,2))