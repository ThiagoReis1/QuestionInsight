x=float(input("digite o numero: "))
k=int(input("digite a constante: "))
s=1
n=1
sinal=-1

while(k>n):
	s=s+pow(x,n)*sinal
	n=n+1
	sinal=sinal*(-1)
print(round(s,7))	