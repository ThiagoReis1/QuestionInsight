from numpy import *

v = array(eval(input("Insira o preco: ")))

for i in range(size(v)):
	if i > 180:
		m = sum(v) / size(v)
		print(m)
	

		