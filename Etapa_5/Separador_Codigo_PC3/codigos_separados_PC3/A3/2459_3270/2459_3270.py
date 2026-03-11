Peso = float(input("Peso: "))
Distancia = float(input("Distancia: "))
Codigo = float(input("Codigo: "))
custo = float(input("custo: "))
if(cod==1):	
	icms = 17.0
	servico = (Peso * custo + Distancia * custo) * (1.0 + icms/100)
	print(round(servico, 2))
elif(cod==2):
	icms = 17.5
	servico = (Peso * custo + Distancia * custo) * (1.0 + icms/100)
	print(round(servico, 2))
elif(cod==3):
	icms = 18.0
	servico = (Peso * custo + Distancia * custo) * (1.0 + icms/100)
	print(round(servico, 2))
elif(cod==4):
	icms = 20.0
	servico = (Peso * custo + Distancia * custo) * (1.0 + icms/100)
	print(round(servico, 2))
else:
	print("Entrada ", cod,"invalida")



 