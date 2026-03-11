x = input("dias da semana:")
qnt = int(input("quantidades de pratos consumidos pelo cliente:"))

desconto = 15 / 100
prato_custa = 22
qua = (prato_custa - desconto)

if x == "qua":
	total = (prato_custa * qnt - prato_custa * (qnt * desconto))

else:
	total = qnt * prato_custa

print(round(total,2))