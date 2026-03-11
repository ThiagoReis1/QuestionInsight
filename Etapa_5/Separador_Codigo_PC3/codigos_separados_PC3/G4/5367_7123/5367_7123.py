from numpy import*

v = array(eval(input("digitos do cpf:")))

i = 0
acum = 0

while i < 9 :
	acum = acum + (v[i] * (i+1))
	i = i + 1
	
print(acum%11)