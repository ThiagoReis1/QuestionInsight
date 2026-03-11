from numpy import*

notas = input ("digite: ").upper().split(",")
resul = zeros(5,dtype=int)

for i in range(size(notas)):
	if notas[i] == 'A':
		resul[0] = resul[0] + 1
	if notas[i] == 'B':
		resul[1] = resul[1] + 1
	if notas[i] == 'C':
		resul[2] = resul[2] + 1
	if notas[i] == 'D':
		resul[3] = resul[3] + 1
	if notas[i] == 'E':
		resul[4] = resul[4] + 1
		
print(resul)