from numpy import *

n = eval(str(input("Numero: ")))

for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
	n = n - 1
	if n == 0:
		n = 9
	n =+ 1
# provisorio 
	print(n**3)