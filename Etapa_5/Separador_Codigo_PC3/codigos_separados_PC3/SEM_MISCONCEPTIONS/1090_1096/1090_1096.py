compraA = float(input("valorA:"))
compraB = float(input("valorB:"))
compraC = float(input("valorC: "))
compraD = float(input("valorD: "))
lim = float(input("lim: "))
valor_total = compraA + compraB + compraC + compraD
if (valor_total == lim) or (valor_total < lim):
	menssagem = "Sim"
else:
	menssagem = "Nao"
print(round(valor_total,2))
print(menssagem) 
