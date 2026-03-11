from numpy import*

n = array(eval(input("")))

i = 0
cont = 10000

while i < size(n):
	if n[i] == 1 :
		cont = cont * 2
	
	if n[i] == 2:
		cont = cont
	
	if n[i] == 3:
		cont = cont / 2
	
	if n[i] == 4:
		cont = cont / 4
	i = i + 1
print(round(cont,2))