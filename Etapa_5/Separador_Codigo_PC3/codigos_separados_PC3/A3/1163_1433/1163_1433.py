lambari_inicial = int(input("Populacao inicial de lambaris: "))
tucunare_inicial = int(input("Populacao inicial de tucunares: "))

lb_crs = int(input("Taxa de crescimento: "))
tc_crs = int(input("Taxa de crescimento: "))

while(lambari_inicial != tucunare_inicial):
	lambaris = lambari_inicial - tucunare_inicial
	