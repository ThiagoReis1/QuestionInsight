ra = input("codigo do cargo: ")
ra2 = float(input("salario do ninja: "))

if ra == "101":
	da = ra2 + (ra2*(10/100))
	da1 = "Aumento de 10 por cento"
else:
	da = ra2 + (ra2*(30/100))
	da1 = "Aumento de 30 por cento"

print(round(da, 2))
print(da1)