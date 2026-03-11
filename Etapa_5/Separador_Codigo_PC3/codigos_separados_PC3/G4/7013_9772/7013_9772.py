x= int(input(''))
y= int(input(''))
numero= x
soma = 0 

while (numero <= y): 
	if numero % 2 == 0:
		soma = soma + numero
	numero = numero + 1
print(soma)