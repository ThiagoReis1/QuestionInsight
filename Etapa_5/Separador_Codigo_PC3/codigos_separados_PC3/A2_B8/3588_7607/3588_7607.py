from numpy import*

pontos = array(eval(input("Digite a pontuacao: ")))

ponto_inicial = 10000
i = 0

while i < len(pontos):
	if pontos[i] == 1:
		ponto_inicial *= 2
	elif pontos[i] == 2:
		ponto_inicial = ponto_inicial
	elif pontos[i] == 3:
		ponto_inicial /= 2
	elif pontos[i] == 4:
		ponto_inicial /= 4
		
	i += 1
	
print(round(ponto_inicial,2))
