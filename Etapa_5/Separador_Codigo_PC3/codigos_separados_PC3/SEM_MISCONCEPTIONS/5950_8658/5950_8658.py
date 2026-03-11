tp = input("T ou P: ").upper()
fatia = int(input("quantidade de fatias: "))
cap = int(input("quantidade de cappuccinos: "))

if tp == "T":
	valor = fatia*6 + cap*4.5
else:
	valor = fatia*5 + cap*4.5
print(round(valor, 2)