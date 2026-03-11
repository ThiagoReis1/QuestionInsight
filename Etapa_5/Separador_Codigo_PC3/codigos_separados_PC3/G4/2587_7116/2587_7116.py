from numpy import*

velo = array(eval(input(": ")))
vel1 = velo[0] * 1.50
cont = 0

for i in range(size(velo)):
	if velo[i] > vel1:
		print(i)
		cont = cont + 1
print(cont)
