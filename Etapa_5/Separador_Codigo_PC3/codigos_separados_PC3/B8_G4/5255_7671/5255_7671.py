#Ecercicio dos Correios

p = float(input("Qual o peso do produto? "))

d = float(input("Qual a distancia do local origem para o destino? "))

c = int(input("Qual o numero do codigo? "))

if(c == 1):
	total = ((p * 25 + d * 0.10) * (1.0 + 17 / 100))
	print(round(total,2))
elif(c == 2):
	total = ((p * 25 + d * 0.10) * (1.0 + 17.5 / 100))
	print(round(total,2))
elif(c == 3):
	total = ((p * 25 + d * 0.10) * (1.0 + 18 / 100))
	print(round(total,2))
elif(c == 4):
	total = ((p * 25 + d * 0.10) * (1.0 + 20 / 100))
	print(round(total,2))