from numpy import *

quant = zeros(4, dtype=int)

notas= input().split(',')

for i in range(len(notas)):
	if(notas[i]=='C'):
		quant[0] = quant[0] + 1
	elif(notas[i]=='D'):
		quant[1] = quant[1] + 1
	elif(notas[i] =='V'):
		quant[2] = quant[2] + 1
	elif(notas[i]=='U'):
		quant[3] = quant[3] + 1
		
print(quant)