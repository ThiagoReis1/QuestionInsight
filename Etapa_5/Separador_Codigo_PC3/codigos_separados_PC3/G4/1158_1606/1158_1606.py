a=int(input("Digite o numero de tracajás:"))
b=float(input("Digite a taxa de crescimento em %:"))
c=int(input("Digite o numero de roubos:"))
t=1
p=a*b
while(p<=0):
	t=t+1
	p=a*b-c-(500*t)
print(t)
		 