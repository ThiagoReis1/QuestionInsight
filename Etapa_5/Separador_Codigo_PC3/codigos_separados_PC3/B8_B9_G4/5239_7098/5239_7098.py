nota = float(input("valor da nota: "))

if nota < 0 or nota > 10:
	print("ERRO")
elif nota >= 9.0:
	print("A")
elif nota >= 8.0 and nota < 9.0:
	print("B")
elif nota >= 7.0 and nota < 8.0:
	print("C")
elif nota >= 6.0 and nota < 7.0:
	print("D")
elif nota >= 4.0 and nota < 6.0:
	print("E")
elif nota < 4.0:
	print("F")