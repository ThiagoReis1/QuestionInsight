a = float(input("Peso do produto: "))
b = float(input("Distancia entrega: "))
codigo = float(input("Codigo: "))

ror = 17
ron = 17.5
am = 18
rj = 20

custo_a = a * 25
custo_b = b * 0.10
total = custo_a + custo_b

if(codigo == 1):
	parcela = 1 + (ror / 100)
	print(round(total * parcela,2))
	
elif(codigo == 2):
	parcela = 1 + (ron /100)
	print(round(total * parcela,2))

elif(codigo == 3):
	parcela = 1 + (am/100)
	print(round(total * parcela,2))
	
elif(codigo == 4):
	parcela = 1 + (rj/100)
	print(round(total * parcela,2))
