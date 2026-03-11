peso = float(input("Informe o peso do produto: "))
distancia = float(input("Informe a distancia entre o ponto de origem e o destino: "))
codigo = int(input("Informe o codigo do estado de destino: "))

if(codigo == "Roraima"):
	servico = (peso * (peso * 25) + (distancia * 0.10)) * (1.0 + (17 / 100))
	print(round(servico, 2))
elif(codigo == "Rondonia"):
	servico = (peso * (peso * 25) + (distancia * 0.10)) * (1.0 + (17.5 / 100))
	print(round(servico, 2))
elif(codigo == "Amazonas"):
	servico = (peso * (peso * 25) + (distancia * 0.10)) * (1.0 + (18 / 100))
	print(round(servico, 2))
else:
	servico = (peso * (peso * 25) + (distancia * 0.10)) * (1.0 + (20 / 100))
	