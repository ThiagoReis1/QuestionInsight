from numpy import*
nome = array(eval(input("")))
a = sum(nome)
b = a - (a%80)*5
c = nome[0:-1]
if(c<=80.0):
	print(a)
else:
	print(b)