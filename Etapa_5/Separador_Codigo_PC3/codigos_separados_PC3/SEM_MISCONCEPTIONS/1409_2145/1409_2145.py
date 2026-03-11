ataque = input("Tipo de ataque? (espada/cauda): ")
D1 = int(input("Digite o primeiro valor sorteado: "))
D2 = int(input("Digite o segundo valor sorteado: "))
D3 = int(input("Digite o terceiro valor sorteado: "))
D4 = int(input("Digite o quarto valor sorteado: "))

#ataque com espadas flamejantes
N = (D1 + D2 + D3 + D4) / 4
dano_espada = 4 * (N + 6)

#ataque com cauda constritora
dano_cauda = (D1 + D2 + D3) * D4

if(ataque.lower() == "espada"):
	print(dano_espada)
else:
	print(dano_cauda)