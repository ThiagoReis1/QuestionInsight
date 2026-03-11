c=float(input()) #valor da casa
d=float(input()) #valor inicial depositado
m=float(input()) #deposito mensal fixo
j=float(input()) #a taxa de juros

s=d #saldo inicial
t=0 #tempo

if ((c> 0) and (d>0) and (m>0) and (j>0)): #Condicao de entradas validas
	while	(s < c):
		s=round(s+s*j/100+m,2)
		t=t + 1
	print(t)
else:
	print("Dados incorretos")