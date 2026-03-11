
resposta = input()

satisfeitos = 0

while(resposta.upper() != 'X'):
	if(resposta.upper() == 'S'):
		satisfeitos += 1
		
	resposta = input()
		

print(satisfeitos)