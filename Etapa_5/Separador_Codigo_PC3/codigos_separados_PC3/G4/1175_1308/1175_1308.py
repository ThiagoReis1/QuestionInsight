from math import*
N=float(input('Quantidade de termos:'))
i=0
p=1
s=-1
S=0
while i<N:
	S=S+(s*sqrt(p))/(6+(2*p+1))
	i=i+1
	p=p+1
	s=-s
print(round(S,5))	
