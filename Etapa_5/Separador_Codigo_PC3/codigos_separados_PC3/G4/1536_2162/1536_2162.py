from math import*
x = float(input("valor neperiano:"))
k = int(input("valor neperiano:"))
soma = 0
t = 0
while(t<k):
	soma=soma+((-1)**t)*(x**(t+1))/((t+1))
	t=t+1
print(round(soma,10))