from numpy import *

estados = input("Estados: ").upper().split(',')

quant = zeros(5, dtype = int)

for i in range(len(estados)):
	if estados[i] == 'AC':
		quant[0] = quant[0] + 1
	elif estados[i] == 'AM':
		quant[1] = quant[1] + 1
	elif estados[i] == 'PA':
		quant[2] = quant[2] + 1
	elif estados[i] == 'RO':
		quant[3] += 1
	elif estados[i] == 'RR':
		quant[4] += 1

print(max(quant))
print(quant)