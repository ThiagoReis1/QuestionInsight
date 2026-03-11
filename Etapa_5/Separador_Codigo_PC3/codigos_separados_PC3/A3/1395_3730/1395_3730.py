valor= float(input("Valor ganho pelo funcionario: "))

preco = float(input("dinheirooooooooooooooooo: "))

if (preco <= 1000):
	edo = (preco * 0.05 )

else:
	edo = (preco)+(preco * 0.05)+ (preco*0.10)
print(round(edo, 2))