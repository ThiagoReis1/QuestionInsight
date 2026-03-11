r = 7.00
m = 6.00
b = 3.00
o = 5.00

a = float(input("Quantidade de ramen: "))
b = float(input("Quantidade de menma: "))
c = float(input("Quantidade de bolinho de arroz: "))
d = float(input("Quantidade de onigi: "))

consumo = (a+b+c+d)
desconto = consumo*0.1

if (consumo <= 42):
	print(round(consumo, 2))

else:
	print(round(consumo - desconto, 2))
