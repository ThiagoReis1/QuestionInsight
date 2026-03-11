from numpy import* 

numero = eval(input("Digite um valor:"))
s = zeros(size(numero),dtype=int)

for i in range(size(numero)):
	if numero[i] == 7:
		s[i] = 49
	else:
		s[i] = numero[i]**2
print(s)