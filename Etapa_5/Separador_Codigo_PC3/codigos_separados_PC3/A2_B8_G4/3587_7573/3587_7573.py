from numpy import * 

vt = array(eval(input('Num: ')))

i = 0
cont = 100

while(i < size(vt)):
	if (vt[i] == 1):
		cont = cont * 5
	elif(vt[i] == 2):
		cont = cont * 3
	elif(vt[i] == 3):
		cont = cont 
	elif(vt[i] == 4):
		cont = cont/2
	i = i + 1

print(round(cont,2))