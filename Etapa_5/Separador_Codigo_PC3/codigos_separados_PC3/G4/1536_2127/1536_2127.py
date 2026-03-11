x=float(input("valor de x:"))
k=int(input("valor de k:"))
soma=0
sinal=1
r=1
n=1
while(r<=k):
	soma=soma+sinal*x**r/n
	r=r+1
	n=n+1
	sinal=-sinal
print(round(soma-x+1,10))