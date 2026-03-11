nome_ataque = input()
dado1 = int(input())
dado2 = int(input())
dano_ale = dado1 + dado2
if (nome_ataque == 'FURIA') and (dano_ale >= 2) and (dano_ale <= 16):
	dano_fixo = 10
	dano_total = dano_fixo + dano_ale
	print(dano_total)
elif (nome_ataque == 'GRITO') and (dano_ale >= 2) and (dano_ale <= 16):
	dano_fixo = 6
	dano_total = dano_fixo + dano_ale
	print(dano_total)
elif (nome_ataque == 'TOQUE') and (dano_ale >= 2) and (dano_ale <= 16):
	dano_total = dano_ale**2
	print(dano_total)
else:
	print("Entrada invalida")
	