from numpy import *
s = input("insira a sequencia: ").upper().split(',')
saida = zeros(4 , dtype = int)

for i in range(size(s)):
	if   s[i] == "A":
		saida[0] += 1
	elif s[i] == "P":
		saida[1] += 1
	elif s[i] == "D":
		saida[2] += 1
	elif s[i] == "M":
		saida[3] += 1

	
print(saida)