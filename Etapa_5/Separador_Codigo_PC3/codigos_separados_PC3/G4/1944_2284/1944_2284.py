nome = input("Nome do Aminoácido: ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

pm1 = (C*6) + (H*13) + N + (O*2)

pm2 = (C*6) + (H*15) + (N*2) + (O*2)

if (nome == "leucina"):
	print(round(pm1, 2))
else:
	print(round(pm2, 2))