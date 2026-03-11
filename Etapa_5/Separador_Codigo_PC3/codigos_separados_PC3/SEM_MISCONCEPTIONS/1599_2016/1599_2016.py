from numpy import*
c = array(eval(input("custos: ")))
i=0
soma = 0
soma2 = 0

while (i<size(c)):
	if(c[i]>=80.0):
		soma = c[i]*0.85+soma
		i=i+1
	else:
		soma2 = c[i]+soma2
		i=i+1
final=soma+soma2
print(round(final,2))