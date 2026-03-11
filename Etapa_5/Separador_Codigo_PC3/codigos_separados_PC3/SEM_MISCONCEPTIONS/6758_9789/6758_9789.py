diaria = 100
quantidade_de_dias = int(input("digite um numero: "))

if quantidade_de_dias < 7:
	add = 15
elif quantidade_de_dias == 7:
	  add = 12
else:
	add = 10

total = (diaria * quantidade_de_dias) + add

print(round(total, 2))
