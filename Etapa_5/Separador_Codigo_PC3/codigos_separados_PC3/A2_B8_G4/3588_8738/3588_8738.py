from numpy import *
num = array(eval(input("alvos acertados: ")))

i = 0
cont = 10000

while i < size(num):
	if num[i] == 1:
		cont = cont * 2
	elif num[i] == 2:
		cont = cont 
	elif num [i] == 3:
		cont = cont / 2
	elif num[i] == 4:
		cont = cont / 4
	i = i + 1 
print(round(cont, 2))
	
