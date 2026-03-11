escolhendo= input("B para fatia de bolo ou S para salgado: ")

if (escolhendo.upper() == "B"):
	Bolo= int(input("quantidade de fatias de bolo: "))
	valor= Bolo*5
else:
	salgado=int(input("quantidade de salgados: "))
	valor= salgado*4

cap=int(input("quantidade de cappuccinos: "))
valor2= cap*7.50

print(round(valor+valor2,2))