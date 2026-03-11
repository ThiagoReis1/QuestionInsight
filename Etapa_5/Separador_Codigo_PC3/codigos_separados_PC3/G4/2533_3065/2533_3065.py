V = float(input("V: "))
C = float(input("C: "))
j = float(input("J: "))

soma=V
i=0
if(V<=0)or(C<=0)or(j<=0):
	print("Dados incorretos")
else:
	while(V>0)and(C>0)and(j>0):
		soma=soma*j
		i=i+1
print(round(soma,2))	