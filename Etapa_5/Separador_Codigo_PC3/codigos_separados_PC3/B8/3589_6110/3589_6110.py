from numpy import * 
acertou = array(eval(input("Digite o numero do alvo acertado: ")), dtype=int)

pontos = 0

for i in range(size(acertou)):
	if(acertou[i] == 1):
		pontos = pontos + 80
		i = i + 1
	elif(acertou[i] == 2):
		pontos = pontos  + 40
		i = i + 1
	elif(acertou[i] == 3):
		pontos = pontos + 20
		i = i + 1
	elif(acertou[i] == 4):
		pontos = pontos + 10
		i = i + 1 
print(pontos)
