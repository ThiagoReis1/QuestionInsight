s=float(input("valor do sitio: "))
d=float(input("valor inicial depositado: "))
m=float(input("deposito mensal fixo: "))
j=float(input("taxa de juros: "))

cont=0
p=0

if(s<0 or d<0 or m<0 or j<0):
	print("Dados incorretos")
else:
	while(s>p):
		z=(d*j/100)+d
		p=(z+m)*(j/100)
		cont=cont+1
		m=m*cont
print(z)
print(p)
print(cont)
print(m)