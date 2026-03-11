from numpy import*
a = array(eval(input("digite o vetor")))
i=0
soma = 0
while (i < size(a)):
	if a[i]==1:
		soma= soma + 100
	elif a[i]== 2:
		soma = soma + 60
	elif a[i] == 3:
		soma = soma + 20
	elif a[i]== 4:
		soma = soma + 0
	i = i + 1
print(soma)
	