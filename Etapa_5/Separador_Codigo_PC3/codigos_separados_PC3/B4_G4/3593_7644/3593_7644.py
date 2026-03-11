from numpy import *
n = eval(input("Valor de numeros: "))
nt = 200
if(n == 1):
	vt = nt/2
elif(n == 2):
	vt = nt*3
elif(n == 3):
	vt = nt/2
elif(n == 4):
	vt = nt*3
elif(n == 5):
	vt = nt/2
else:
	vt = nt*3
print(round(vt, 2))