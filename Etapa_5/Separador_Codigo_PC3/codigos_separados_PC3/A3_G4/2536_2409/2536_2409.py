c = float(input("valor da casa: "))
d = float(input("valor inicial do deposito: "))
m = float(input("deposito mensal: "))
j = float(input("taxa de juros: "))

mes = 0
soma = 0

c = float(input("valor da casa: "))
d = float(input("valor do deposito: "))
m = float(input("deposito mensal: "))
j = float(input("taxa de juros: "))

mes = 0
soma = 0

#while(soma <= c):
#	poupanca = (round(d + m + j),2)
#	mes = mes + 1
#	soma = soma + 1

#print(soma)
while(d + m <= c):
	poupanca = (round(m + j/100),2)
	mes = mes + 1
	soma = soma + 1
	m = float(input("deposito mensal: "))
print(soma)