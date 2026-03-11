a = float(input())
f = float(input())

percentual_de_ganho = f - a

if(percentual_de_ganho > 0):
	print("saldo positivo")
if(percentual_de_ganho == 0):
	print("sem variacao")
if(percentual_de_ganho < 0):
	print("saldo negativo")
	