from numpy import *

x = array(eval(input()))

i = 0
total = 0

while(i<size(x)):
	if(x[i] == 1):
		total = total + 100
	elif(x[i] == 2):
		total = total + 60
	elif(x[i] == 3):
		total = total + 20
	elif(x[i] == 4):
		total = total + 0
	i = i + 1
print(total)
		