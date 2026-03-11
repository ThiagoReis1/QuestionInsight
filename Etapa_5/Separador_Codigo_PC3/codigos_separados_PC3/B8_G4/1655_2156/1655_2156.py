from numpy import*

estados = input("Digite as siglas dos estados: ").split(',')

AC = 0
AM = 0
PA = 0
RO = 0
RR = 0

i = 0

while i < len(estados):

	if (estados[i] == "AC"):
		AC = AC+1
	elif (estados[i] == "AM"):
		AM = AM+1
	elif (estados[i] == "PA"):
		PA = PA+1
	elif (estados[i] == "RO"):
		RO = RO+1
	elif (estados[i] == "RR"):
		RR = RR+1
	i = i+1

saida = zeros(5, dtype = int)

saida[0] = AC
saida[1] = AM
saida[2] = PA
saida[3] = RO
saida[4] = RR

print(max(saida))
print(saida)