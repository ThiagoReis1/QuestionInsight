from numpy import * 

x = array(eval(input("Quantidade de ubs: ")))
soma = 0

for i in range(1, len(x)):
	if(x[i]>=x[0]):
		print(i)
		soma = soma + 1
print(soma)