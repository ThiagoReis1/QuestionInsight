altura_max = 1.75
taxa_max = 0.01

altura_desconhecido = float(input('aim:'))
taxa_desconhecido = float(input('tcrm:'))

data = 0

while altura_desconhecido < altura_max:
	altura_max = altura_max + taxa_max
	altura_desconhecido = altura_desconhecido + taxa_desconhecido
	data += 1
	
print(data)