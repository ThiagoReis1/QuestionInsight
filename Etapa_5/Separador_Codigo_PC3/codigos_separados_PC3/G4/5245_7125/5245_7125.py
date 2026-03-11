s = float(input("salario:"))
print("Entrada: R$ ",s)

if 0 < s:
	if s <= 800:
		x = s + (s * 0.50)
	else:
		if 800 < s <= 1000:
			x = s + (s * 0.40)
		else:
			if 1000 < s <= 1200:
				x = s + (s * 0.30)
			else:
				if 1200 < s <= 1400:
					x = s + (s * 0.20)
				else:
					if 1400 < s <= 1600:
						x = s + (s * 0.10)
					else:
						x = s + (s * 0.05)
		y = round(x,2)
		print("Novo salario: R$ ",y)
else:
	print("Dado invalido")

