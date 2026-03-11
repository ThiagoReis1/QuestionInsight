from numpy import*
v = array(eval(input("Digite o valores a ser somados: ")))

soma = 0

for i in range(size(v)):
	if(v[i] == 0):
		soma = 0
	else:
		soma  = soma  + v[i]
print(soma)
		