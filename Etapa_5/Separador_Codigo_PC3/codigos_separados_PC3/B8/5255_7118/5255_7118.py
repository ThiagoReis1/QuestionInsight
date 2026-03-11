peso = float(input(""))
distancia = float(input(""))
codigo = int(input(""))

custo1 = peso * 25
custo2 = distancia * 0.10

if codigo == 1:
	servico = (peso * custo1 + distancia * custo2) * (1.0 + 0.17)
	print(round(servico,2))
elif codigo == 2:
	servico = (peso * custo1 + distancia * custo2) * (1.0 + 0.175)
	print(round(servico,2))
elif codigo == 3:
	servico = (peso * custo1 + distancia * custo2) * (1.0 + 0.18)
	print(round(servico,2))
elif codigo == 4:
	servico = (peso * custo1 + distancia * custo2) * (1.0 + 0.20)
	print(round(servico, 2))
