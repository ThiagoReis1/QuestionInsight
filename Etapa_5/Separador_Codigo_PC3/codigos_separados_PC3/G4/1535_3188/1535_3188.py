x=float(input("Digite x:"))
k=int(input("Digite k:"))

n=0

soma=0

z=1
while(n<k):
	termoa=((-1)**n)* (x**(z)/(z))
	soma=soma+termoa
	z=z+2
	n=n+1
	
print(round(soma,6))
	
	