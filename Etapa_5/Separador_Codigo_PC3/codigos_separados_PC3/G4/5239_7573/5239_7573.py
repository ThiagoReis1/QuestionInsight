nt = float(input("Digte a nota: "))

if (nt < 0 or nt >10):
	print("ERRO")
elif(nt >= 9.0):
	print("A")
elif(nt >= 8.0):
	print("B")
elif(nt >= 7.0):
	print("C")
elif(nt >= 6.0):
	print("D")
elif(nt >= 5.0):
	print("E")
else:
	print("F")
	