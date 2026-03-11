#Correios
peso = int(input("entre com o peso: "))
distancia = int(input("entre com a distancia: "))
codigo = int(input("entre com o codigo: "))
kg = 25.00
km = 0.10
if(codigo>=1) and (codigo<=4):
	if(codigo == 1):
		icms = 17.0
		servico = ((peso*kg)+(distancia*km))*(1.0+(icms/100))
		print(servico)
	elif(codigo == 2):
		icms = 17.5
		servico = ((peso*kg)+(distancia*km))*(1.0+(icms/100))
		print(servico)
	elif(codigo == 3):
		icms = 18.0
		servico = ((peso*kg)+(distancia*km))*(1.0+(icms/100))
		print(servico)
	elif(codigo == 4):
		icms = 20.0
		servico = ((peso*kg)+(distancia*km))*(1.0+(icms/100))
		print(servico)
else:
	print("Dados invalidos")
