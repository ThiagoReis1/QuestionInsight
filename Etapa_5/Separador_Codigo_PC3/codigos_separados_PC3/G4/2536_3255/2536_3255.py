c= float(input("Valor da casa: "))
d= float(input("Valor inicial: "))
m= float(input("Deposito mensal: "))
j= float(input("Juros: "))

tj= j / 100
i=0
saldo= d 
if(c > 0) and (d > 0) and (m > 0) and (j > 0):
	while(saldo < c):
		rend= saldo  * tj 
		saldo= round(saldo + m + rend,2) 
		i=i + 1
	print(i)
else:
	print("Dados incorretos")