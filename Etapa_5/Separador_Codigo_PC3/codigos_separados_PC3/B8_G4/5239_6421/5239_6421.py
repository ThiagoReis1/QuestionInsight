nota = float(input("digite as notas: "))

if (nota > 10) or (nota < 0):
	print("ERRO")
elif (nota >= 9) and ( nota <= 10):
	print("A")
elif (nota >= 8) and (nota < 9):
	print("B")
elif (nota >= 7) and (nota < 8):
	print("C")
elif (nota >= 6) and (nota < 7):
	print("D")
elif (nota >= 4) and (nota < 6):
	print("E")
elif (nota < 4) and (nota >= 0):
	 print("F")