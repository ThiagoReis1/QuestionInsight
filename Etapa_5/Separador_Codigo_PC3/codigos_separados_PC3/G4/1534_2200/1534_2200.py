from math import* 
x=float(input("numero:"))
k=int(input("numero:"))
soma=0
t=0
while(t < k):
	soma=soma+((1)**t)*(x**(2*t+1))/(2*t+1)
	t=t+1
print(round(soma,7))
	
	
