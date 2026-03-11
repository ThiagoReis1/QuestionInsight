from numpy import *

v = array(eval(input("Quais foram as faces: ")))

i = 0
cont = 0

while i < len(v):
	if v[i] == 1:
		cont = cont + 10
	elif v[i] == 2:
		cont = cont + 5
	elif v[i] == 3:
		cont = cont
	elif v[i] == 4:
		cont = cont + 5
	elif v[i] == 5:
		cont = cont + 20
	elif v[i] == 6:
		cont = cont + 10
		
	i = i + 1
print(cont)