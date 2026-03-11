peso = float(input("Peso: "))
distancia = float(input("Distancia: "))
codigo = float(input("Codigo: "))
if(codigo == 1):
	icms = 17
	servico = (peso*25 + distancia*0.1) * (1 +icms/100)
	print(round(servico,2))
elif(codigo == 2):
	icms = 17.5
	servico = (peso*25 + distancia*0.1) * (1 +icms/100)
	print(round(servico,2))
elif(codigo == 3):
	icms = 18
	servico = (peso*25 + distancia*0.1) * (1 +icms/100)
	print(round(servico,2))
elif(codigo == 4):
	icms = 20
	servico = (peso*25 + distancia*0.1) * (1 +icms/100)
	print(round(servico,2))