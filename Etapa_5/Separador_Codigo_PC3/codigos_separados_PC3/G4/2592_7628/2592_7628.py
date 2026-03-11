from numpy import*
a=array(eval(input()))
i=1

soma=0

while i<size(a):
	if a[i]>=a[0]:
		print(i)
		soma=soma+1
	i=i+1
print(soma)