nome = input("Nome do Aminoácido: ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

pm1 = (C*6) + (H*15) + (N*4) + (O*2)
pm2 = (C*9) + (H*11) + (N*1) + (O*3)
pm3 = (C*11) + (H*11) + (N*2) + (O*2)

if (nome == "Arginina".upper()):
	print(round(pm1, 2))
elif (nome == "Tirosina".upper()):
	print(round(pm2, 2))
elif (nome == "Triptofano".upper()):
	print(round(pm3, 2))
else:
	print("Entrada:", nome.upper())
	print("Dado Invalido")