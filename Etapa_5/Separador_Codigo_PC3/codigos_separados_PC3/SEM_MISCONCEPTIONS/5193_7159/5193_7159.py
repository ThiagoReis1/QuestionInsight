preco_ramem = 7.00
preco_menma = 6.00
preco_arroz = 3.00
preco_onigi = 5.00

ramem = float(input())
menma = float(input())
arroz = float(input())
onigi = float(input())

consumo = (ramem * preco_ramem) + (menma * preco_menma) + (arroz * preco_arroz) + (onigi * preco_onigi)
desconto = consumo * 0.1

if(consumo <= 42.00):
	total = consumo - 3.00
else:
	total = consumo - desconto

print(round(total, 2), "ryous")