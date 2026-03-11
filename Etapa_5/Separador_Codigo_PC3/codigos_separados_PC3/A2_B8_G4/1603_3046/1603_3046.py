from numpy import *
v = array(eval(input("v: ")))

i = 0
acum = 0

while(i < size(v)):
	if(v[i] == 1):
		acum = acum + 80
	elif(v[i] == 2):
		acum = acum + 40
	elif(v[i] == 3):
		acum = acum + 20
	elif(v[i] >= 4):
		acum = acum
	i = i + 1
print(acum)