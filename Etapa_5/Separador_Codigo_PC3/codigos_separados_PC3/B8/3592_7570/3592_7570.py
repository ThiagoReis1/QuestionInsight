from numpy import*
x = array(eval(input()))
i = 0
total = 100
while(i < size(x)):
	if(x[i] == 1):
		total = total * 1
	elif(x[i] == 2):
		total = total * 2
	elif(x[i] == 3):
		total = total / 3
	elif(x[i] == 4):
		total = total * 4
	elif(x[i] == 5):
		total = total / 5
	elif(x[i] == 6):
		total = total * 6
	i = i + 1
print(round(total, 2))