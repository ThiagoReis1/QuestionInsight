from numpy import*
from numpy.linalg import*
A=array(eval(input("Alimentos:")))
Q=array((eval(input("Quantidade:"))))
n=size(Q)
x=zeros(n, dtype=int)
k=zeros(n, dtype=int)
y=0

for i in range(n):
	if(A[i]== "BANANA"):
		x[i]=0.97
		k[i]=Q[i]*x[i]
		y=y+k[i]
	elif(A[i]=="BIFE"):
		x[i]=2.95
		k[i]=Q[i]*x[i]
		y=y+k[i]
		
	elif(A[i]=="FEIJOADA"):
		x[i]=1.27
		k[i]=Q[i]*x[i]
		y=y+k[i]
	elif(A[i]=="OMELETE"):
		x[i]=1.04
		k[i]=Q[i]*x[i]
		y=y+k[i]
	elif(A[i]=="TOMATE"):
		x[i]=0.2
		k[i]=Q[i]*x[i]
		y=y+k[i]

print(y)
