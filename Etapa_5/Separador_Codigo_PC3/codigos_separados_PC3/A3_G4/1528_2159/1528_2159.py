# Entradas
pg = int(input("A quantidade de pontos de força que cada guerreiro tira do troll: "))
p0 = int(input("A quantidade inicial de pontos de força do troll: "))
pr = int(input("A quantidade de pontos de força que o troll recupera: "))

i = 0 		# Contador de rodadas
pontos = 0	# Pontos de força perdidas pelo troll

while p0 > 0:
	p0 = p0 - 5*pg + pr
	i = i + 1
	
print(i)