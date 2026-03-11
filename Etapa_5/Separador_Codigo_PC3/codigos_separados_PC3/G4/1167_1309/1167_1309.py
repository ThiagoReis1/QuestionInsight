N=int(input("digite o numero N de termos:"))

t=1
soma=0
n=1
d=1

while(t<=N):
	if(n%2 !=0):
		termo= -n**2/(7+d)
		soma=soma + termo
		n=n+1
		d=d+2
		t=t+1
	else:
		termo= n**2/(7+d)
		soma=soma + termo
		n=n+1
		d=d+2
		t=t+1
print(round(soma,11))