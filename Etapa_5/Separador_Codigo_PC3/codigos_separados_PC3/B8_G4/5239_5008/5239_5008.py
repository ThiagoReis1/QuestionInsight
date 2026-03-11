n = float(input("nota: "))
if (n >= 9) and (n <=10):
	print("A")
elif (n >= 8) and (n < 9):
		print("B")
elif (n >= 7) and (n < 8):
		print("C")
elif (n >= 6) and (n < 7):
		print("D")
elif (n >= 4) and (n < 6):
		print("E")
elif (n <= 4) and (n >= 0):
		print("F")
if (n < 0) or (n > 10):
		print("ERRO")