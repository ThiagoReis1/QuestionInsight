from numpy import*
c= array(eval(input("")))
i=0
soma=0
while i<size(c):
	if c[i]>90:
		soma=soma+(c[i]- 6.5)
	else:
		soma=soma+c[i]
	i=i+1
print(round(soma, 2))