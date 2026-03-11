v = int(input("Digite o valor: "))
tx = float(input("taxa %: "))
g = int(input("Digite o valor gasto: "))

renda = v
i = 0
t = tx/100

while(renda >= g):
	renda = v + (v * t)
	soma = renda - g
	
