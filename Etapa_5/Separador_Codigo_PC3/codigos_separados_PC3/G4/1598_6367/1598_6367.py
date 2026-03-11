from numpy import*
a=array(eval(input("Insira o  vetor valores: ")))
i=0
soma=0
while i<size(a):
	if a[i]>90.0:
		soma=soma+(a[i]-6.5)
	else:
		soma=soma+a[i]
	i=i+1
print(round(soma,2))