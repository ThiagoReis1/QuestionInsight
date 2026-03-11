from numpy import*
contagem = [0,0,0,0]
sequencia_gols = input("Digite os gols separados por virgula: ")
gols = sequencia_gols.split(',')
for gol in gols:
		if gol == 'A':
			contagem[0] +=1
		elif gol == 'B':
			contagem[1] +=1
		elif gol == 'C':
			contagem[2] +=1
		elif gol == 'D':
			contagem[3] +=1
contagem = array(contagem)
print(contagem)