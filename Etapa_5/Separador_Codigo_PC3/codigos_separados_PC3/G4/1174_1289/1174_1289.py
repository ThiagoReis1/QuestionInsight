n=int(input("insira n: "))
z=1
i=3
soma=0
while z<=n:
	if z%2==0:
		s=(z**3)/(9+i)
	else:
		s=((z**3)/(9+i))*(-1)
	soma=soma+s
	z=z+1
	i=i+2
print(round(soma,8))