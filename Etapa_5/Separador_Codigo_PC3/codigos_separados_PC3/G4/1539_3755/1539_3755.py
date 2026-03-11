x=float(input('Digite um numero:'))
k=int(input('Qtd de termos:'))
exp=0
s=0
while(exp<k):
	s=s+(((-1)**exp)*(x**exp))
	exp=exp +1
print(round(s,7))