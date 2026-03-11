nter=float(input("Quantidade de termo:"))
x=0
y=1
sinal=-1
Soma=0
while(x<nter):
	Soma=Soma + (sinal*y**3)/(9+(2*y+1))
	y=y+1
	x=x+1
	sinal=-sinal
print(round(Soma,8))