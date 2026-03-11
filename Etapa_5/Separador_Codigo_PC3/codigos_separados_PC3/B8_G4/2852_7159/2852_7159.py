from numpy import*

v = array(eval(input("vetor: ")))

soma = 0

for i in range(size(v)):
	if(v[i] != 88):
		soma = soma + v[i]
	elif(v[i] == 88):
		soma = soma / 2
print(soma)