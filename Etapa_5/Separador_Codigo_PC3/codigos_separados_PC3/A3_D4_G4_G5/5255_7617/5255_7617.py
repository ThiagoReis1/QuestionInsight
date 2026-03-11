peso = float(input('Digite o peso do produto (kg): '))
distancia = float(input('Digite a distancia (km): '))
codigo = int(input('Digite o codigo: '))

# Formula
# total = (peso * custoPeso + distancia * custoDistancia) * (1.0 + icms/100 )

custo_peso = 25 * peso
custo_distancia = 0.10 * distancia
icms = 0

resultado = 0

def calcular(icms):
	return round((custo_peso +custo_distancia) * ((1.0 + icms)),2)

if(codigo == 1):
	icms = 17/100
	print(calcular(icms))
elif (codigo == 2):
	icms = 17.5 / 100
	print(calcular(icms))
elif (codigo == 3):
	icms = 18 / 100
	print(calcular(icms))
else:
	icms = 20 / 100
	print(calcular(icms))
	
#print(round(total, 2))
	
	