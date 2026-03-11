from numpy import*

f = array(eval(input("Faces do dado:")))

i = 0
soma = 0

while (i < size(f)):
	if (f[i] == 1):
		soma = soma + 10
	if (f[i] == 2):
		soma = soma + 5
	if (f[i] == 3):
		soma = soma
	if (f[i] == 4):
		soma = soma + 5
	if (f[i] == 5):
		soma = soma + 20
	if (f[i] == 6):
		soma = soma + 10
	i = i + 1
print(soma)