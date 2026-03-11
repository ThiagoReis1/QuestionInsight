#banshee, um morto-vivo
#Ataque da banshe: grito aterrorizante: causa um dano fixo de 6 pontos
#mais um aleatorio de 2 a 16 sorteados com dois dados de oito
#segundo ataque: toque da morte: causa um dano aleatorrio correspondente
#ao quadrado da soma de pontos obtidos em um sorteio com dois dados de oito
A1=input("Nome do ataque da Banshee")
D1 = int(input("Dado 1?"))
D2 = int(input("Dado 2?"))
A = (A1).lower()
D = D1 + D2
G1 = 6 + D
G2 = (D)**2
if A==("toque"):
	print(G2)
else:
	print(G1)