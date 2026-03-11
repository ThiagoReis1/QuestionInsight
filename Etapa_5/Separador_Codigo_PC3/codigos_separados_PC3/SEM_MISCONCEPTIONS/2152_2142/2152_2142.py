from numpy import *

cont = zeros(2, dtype = int)

matricula = array(eval(input("Digite as matrículas: ")))
im = 0
par = 0
for i in range(size(matricula)):
	if(matricula[i] % 2 == 0):
		par = par + 1
	elif(matricula[i] % 2 != 0):
		im = im + 1
cont[0] = par
cont[1] = im
x = zeros(im, dtype = int)
x[0] =