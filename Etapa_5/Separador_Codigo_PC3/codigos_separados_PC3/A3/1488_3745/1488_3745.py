c = int(input("Digite o consumo de minutos: "))

if(c >= 0 and c <= 100):
	valor = c * 1.20 + 1
if(c > 100 and c <=200):
	valor = c * 1.30 + 10
if(c > 200 and c <=300):
	valor = c * 1.40 + 20
if(c > 300):
	valor = c * 1.50 + 25

print(round(valor,2))