# gabriel siza  de oliveira brandão - 21601146
# av.4

valor = int(input("valor:"))
taxa = float(input("digite a taxa"))
gasto = int(input("digite os gastos"))

renda = valor
i=0
taxa=taxa/100

while renda>=gasto:
	renda = valor + (valor*taxa)
	soma = renda - gasto
	valor = soma
	i = i + 1
print(i)