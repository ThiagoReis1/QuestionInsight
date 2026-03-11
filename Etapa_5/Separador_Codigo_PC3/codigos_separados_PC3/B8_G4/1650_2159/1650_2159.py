from numpy import*

# Entrada
cor = (input("Digite as cores: ").upper()).split(',')

p = 0		# Preto
c = 0		# Castanho
r = 0 	# Ruivo
l = 0		# Loiro
b = 0		# Branco

i = 0
while i < len(cor):
	if cor[i] == "P":
		p = p + 1
	elif cor[i] == "C":
		c = c + 1
	elif cor[i] == "R":
		r = r + 1
	elif cor[i] == "L":
		l = l + 1
	elif cor[i] == "B":
		b = b + 1
	i = i + 1
	
saida = zeros(5, dtype = int)
saida[0] = p
saida[1] = c
saida[2] = r
saida[3] = l
saida[4] = b

print(max(saida))
print(saida)