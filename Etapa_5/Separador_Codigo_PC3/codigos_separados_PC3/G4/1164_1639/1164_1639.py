n=int(input("digite aqui o numero de termos da serie:"))

i=1
c=0
j=1
soma=0
sinal=1

while(c<n):
	soma=soma+sinal*((i)**2)/(4+j)
	i=i+1
	j=j+2
	c=c+1
	sinal=-sinal
print(round(soma,8))