# Entradas (Fenilalanina/Tirosina)
amino = input("Digite o nome do aminoácido: ").lower()

# Dados
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

# Condição
if (amino == "fenilalanina"):
	Feni = C*9 + H*11 + O*2 + S
	print(round(Feni,2))
else:
	Tiro = C*9 + H*11 + N + (O*3)
	print(round(Tiro,2))

