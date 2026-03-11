x =float(input(" "))
k = int(input(" "))
cont = 0
expoente = 1
denominador = 1
resposta = 0
while(cont < k):
	resposta = resposta + (x**expoente)/denominador
	cont += 1
	expoente = expoente + 2
	denominador = denominador +2
print(round(resposta,7))