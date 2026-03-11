from math import*

x=float(input("digite:"))
k=int(input("digite:"))

soma=0
i=0
sinal=+1

while(i<k):
	soma=soma+ ((x**(i+1))/(i+1))*sinal
	i=i+1
	sinal=-sinal
	#y=soma/k
print(round(soma-x+1,10))
	