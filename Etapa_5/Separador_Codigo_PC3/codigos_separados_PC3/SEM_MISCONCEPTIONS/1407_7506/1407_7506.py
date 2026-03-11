hp_inicial = int(input())

dado1 = int(input())
dado2 = int(input())
dado3 = int(input())

dano = 10*(dado1 + dado2 + dado3)

hp_final = hp_inicial - dano

if hp_final > 0:
	print(hp_final)
	print("VIVO")
else:
	print(0)
	print("MORTO")