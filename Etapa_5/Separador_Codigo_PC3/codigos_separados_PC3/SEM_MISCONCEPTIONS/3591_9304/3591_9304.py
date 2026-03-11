from numpy import *

dados = eval(input("Face: "))
a = 0
i = 0

for i in range(len(dados)):
	faces = dados[i]
	
	if (faces == 1 or faces == 3 or faces == 5):
		a += 10
	else:
		a+= 5
print(a)