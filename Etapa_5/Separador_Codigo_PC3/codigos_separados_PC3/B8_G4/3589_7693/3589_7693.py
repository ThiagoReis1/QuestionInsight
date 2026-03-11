from numpy import *

j = array(eval(input("Digite os aneis que acertou: ")))

i = 0
cont = 0
while i < size(j):
	if j[i] == 1:
		cont = cont+80
	elif j[i] == 2:
		cont = cont +40
	elif j[i] == 3:
		cont = cont +20
	elif j[i] == 4:
		cont = cont+10
	
	i = i+1
print(cont)
	

	