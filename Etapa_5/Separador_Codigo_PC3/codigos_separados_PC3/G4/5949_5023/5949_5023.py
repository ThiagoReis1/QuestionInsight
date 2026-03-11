a = input("B para fatia de bolo ou C para croissant: ").upper()
q = int(input("Quantidade de fatias: "))
qq = int(input("Quantidade de cappuccinos: "))
vc = qq * 5.5
if (a == "B"):
	t = q * 3 + vc
else:
	t = q * 6 + vc
print(t)