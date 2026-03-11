Distancia = float(input("Digite a distancia que o ninja ira percorrer em km: "))
chakra_do_ninja = float(input("Determine o total de chakra do Ninja: "))
conversao_da_distancia = Distancia * 1000

perda_de_chakra = (30.00 * conversao_da_distancia) / 10

if(perda_de_chakra <= chakra_do_ninja):
	print(round(perda_de_chakra, 2))
	print("vai conseguir")
else :
	print(round(perda_de_chakra, 2))
	print("nao vai conseguir")