from numpy import*
gols = input("Entre com os caracteres referente ao jogador que marcou: ").upper().split(",")

cont = zeros(4,dtype=int)

for i in range(size(gols)):
	if gols[i] == "A":
		cont[0] = cont[0] + 1
	elif gols[i] == "B":
		cont[1] = cont[1] + 1
	elif gols[i] == "C":
		cont[2] = cont[2] + 1
	elif gols[i] == "D":
		cont[3] = cont[3] + 1
		
print(cont)

