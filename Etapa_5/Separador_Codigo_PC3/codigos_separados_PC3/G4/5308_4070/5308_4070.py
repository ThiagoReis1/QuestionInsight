x=float(input("numero real: "))
k=int(input("quantidade de termo da serie: "))

i=1
soma=0

while i<=k:
	tg = i/((i*2)*x)
	soma=soma+tg
	i=i+1
print(round(soma,10))