distancia = float(input("Informe a distancia da corrida em Km: "))
total_de_chakras = float(input("Informe o total de chakras que o ninja possui: "))

d = distancia * 1000
v = (d * 30) / 10

if(v <= total_de_chakras):
	print(round(v, 1))
	print("vai conseguir")
else:
	print(round(v, 1))
	print("nao vai conseguir")