# Leticia Filardi
# Avaliacao 4

valor = int (input ("Valor:"))
taxa = float (input ("Taxa:"))
gasto = int (input ("Gasto:"))

renda = valor
i = 0
t = taxa/100

while (renda >= gasto):
	renda = valor + (valor * t)
	soma = renda - gasto
	valor = soma
	i = i + 1
print (i)