from numpy import*
a=array(eval(input()))
soma=0
for i in range (size(a)):
	if a[i] != 88:
		soma=soma+a[i]
	else:
		soma=soma/2
print(soma)
		