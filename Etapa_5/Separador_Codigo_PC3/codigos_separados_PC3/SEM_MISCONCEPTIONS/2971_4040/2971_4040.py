#Incertable

j = float(input("Initial Tax: "))
price = float(input("Price of the Apartament: "))

#Computation

final_capital = 1500*((1 + j)**36)

print(round(final_capital,2))
if (final_capital > price):
	print("Sim")
else:
	print("Nao")