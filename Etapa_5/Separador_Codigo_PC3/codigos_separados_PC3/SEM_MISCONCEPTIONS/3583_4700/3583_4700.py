from numpy import*

precos = array(eval(input("Digite os precos: ")))

soma = 0

for i in precos:
	if (i>50):
		soma = soma + (i-(i*(8/100)))
	else:
		soma = soma + i

print(round(soma,2))