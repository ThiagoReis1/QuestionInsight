from numpy import *

cor = input("digite as cor dos olhos").upper()
vetcores = zeros(5, dtype = int)

for i in range(len(cor)):
	if(cor[i] == 'P'):
		vetcores[0] = vetcores[0] + 1
	if(cor[i] == 'C'):
		vetcores[1] = vetcores[1] + 1
	if(cor[i] == 'M'):
		vetcores[2] = vetcores[2] + 1
	if(cor[i] == 'V'):
		vetcores[3] = vetcores[3] + 1
	if(cor[i] == 'A'):
		vetcores[4] = vetcores[4] + 1
	
print(max(vetcores))
print(vetcores)