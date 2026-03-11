from numpy import*
v = array(eval(input("Vetor: ")))
soma = 0
for i in range(size(v)):
	if(v[i] != 0):
		soma = soma + v[i]
	elif(v[i] == 0):
		soma = 0
print(soma)