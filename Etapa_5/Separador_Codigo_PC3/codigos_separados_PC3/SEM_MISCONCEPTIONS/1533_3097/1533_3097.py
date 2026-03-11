from math import*
numero=float(input("numero real: "))
termos=int(input("numero de termos k: "))
i=0
soma=0
n=0
while(n<termos):
	t=(numero**(2*i))/(factorial(2*i))
	soma=soma+t
	n=n+1
	i=i+1
print(round(soma,8))
