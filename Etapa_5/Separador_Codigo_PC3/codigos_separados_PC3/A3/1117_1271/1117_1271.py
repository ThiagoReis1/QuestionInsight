pn = float(input("Digite o valor: "))
d = input("Digite o dia: ")
mao = input("Digite S ou N: ")
segunda = "1"
terca = "2"
quarta = "3"
quinta = "4"
sexta = "5"
sabado = "6"
domingo = "7"
print ("Entradas:", pn ,",",d,",",mao)
if pn >=0:
	if d == "1" or d =="2" or d=="3" and mao=="S":
		valor = pn * 0.25
		valor_2 = pn - valor
		valor_total = (round(valor_2 + 20,2))
		print("Valor a pagar: R$",valor_total)
	elif mao=="S":
		valor = pn + 20
		print("Valor a pagar: R$",valor)
	else :
		mao=="N"
		print(round(pn,2))
else:
	print("Dados invalidos")
