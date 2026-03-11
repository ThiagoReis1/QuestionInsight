var1 = int(input("escolha um numero: "))
quociente = (var1 // 41)
resto = (var1 % 41)

if (resto <= 0):
	print(quociente, "sim")
	
else:
	print(resto, "nao")