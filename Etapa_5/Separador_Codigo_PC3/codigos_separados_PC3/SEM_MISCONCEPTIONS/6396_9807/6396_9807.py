from numpy import *

codigo = array(eval(input("insira um numero: ")))
novasenha =  zeros(size(codigo), dtype= int)

for i in range(size(codigo)):
	if codigo[i] == 7:
		novasenha[i] = 14
	else: 
		novasenha[i] = codigo[i]*2
	
print(novasenha)
	