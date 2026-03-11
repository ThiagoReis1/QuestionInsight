cap = int(input("A capacidade N do navio, em número de containers :"))
est = int(input("O estoque inicial de containers :"))
quant = int(input("A que chegam no depósito a cada semana :"))
c = 0
while(est>0):
	tot= est - cap
	est = tot + quant
	c = c + 1
print(c)