s=float(input("valor do sitio: "))
d=float(input("valor inicial: "))
m=float(input("deposito mensal: "))
j=float(input("taxa de juros")) /100

acd = d	#acumulador do deposito
dia=0

while(d<s):
	if((s>0) and (d>0) and (m>0) and (j>0)):
			acd = acd+m+(m*j)
			dia=dia+1
			print(dia, 2)
	else:
print("Dados incorretos")
	