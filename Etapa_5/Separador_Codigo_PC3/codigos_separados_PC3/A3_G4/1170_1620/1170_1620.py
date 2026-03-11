n=int(input("Digite um numero:"))
a=0.0
s=0.0
i=3.0
b=1.0
sinal=1
while(b<=n):
	s=s+(b**2/(1+i))*sinal
	i=i+2
	b=b+1
	sinal=sinal*-1
print(round(s, 7))