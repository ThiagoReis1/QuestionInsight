from numpy import*

a = array(eval(input()))

soma = 0

for i in range(size(a)):
	if (a[i] != 10):
		soma+= a[i]
		
	elif (a[i] == 10):
		soma= soma * 10
		
print(soma)