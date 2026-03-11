n=int(input("N:"))

#contadora
i=1
#acumuladora
se=pow(-n,3)/8+n

sinal=1

while i<=n:
	x=pow(n,3)/8+n+i
	se=se+x
	i=i+1
	sinal=-sinal

print(round(se,5))