from numpy import *

cor = input("digite as cores").upper().split(',')

vetcor = zeros(6, dtype = int)
a = 0
for a in range(size(cor)):
	if(cor[a] == 'MC'):
		vetcor[0] = vetcor[0] + 1
	if(cor[a] == 'C'):
		vetcor[1] = vetcor[1] + 1
	if(cor[a] == 'CM'):
		vetcor[2] = vetcor[2] + 1
	if(cor[a] == 'EM'):
		vetcor[3] = vetcor[3] + 1
	if(cor[a] == 'E'):
		vetcor[4] = vetcor[4] + 1
	if(cor[a] == 'ME'):
		vetcor[5] = vetcor[5] + 1

print(max(vetcor))
print(vetcor)
