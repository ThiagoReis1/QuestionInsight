from numpy import*
cont = zeros(4, dtype=int)
pac = input(" :").upper().split(',')

for i in range(size(pac)):
	if(pac[i] == 'O'):
		cont[0] = cont [0] + 1
	elif(pac[i] == 'D'):
		cont[1] = cont [1] + 1
	elif(pac[i] == 'N'):
		cont [2] = cont[2] + 1
	elif(pac[i] == 'C'):
		cont [3] = cont[3] +1
		
print(cont)
