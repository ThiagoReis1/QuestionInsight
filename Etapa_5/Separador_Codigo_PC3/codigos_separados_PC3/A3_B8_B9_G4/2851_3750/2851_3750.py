from numpy import * 
v = array(eval(input("")))
soma = 0
i = 0
n = 0
for n in v :
		if(n != 99):
			soma = soma + n
		elif(n == 99):
			soma = soma * 2
print(soma)