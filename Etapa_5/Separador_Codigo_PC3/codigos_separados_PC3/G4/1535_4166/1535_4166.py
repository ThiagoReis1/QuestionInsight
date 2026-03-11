x=float(input("x:"))
k=int(input("termos da serie:"))

t=x
n=1

while(k>n):
	restante=(-1)**n*(x**(2*n+1))/(2*n+1)
	t=t+restante
	n=n+1
print(round(t, 6))