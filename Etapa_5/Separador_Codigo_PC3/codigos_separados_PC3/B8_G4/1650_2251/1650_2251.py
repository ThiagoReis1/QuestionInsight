from numpy import*
cor = input(": ").upper().split(',')
cont = zeros(5, dtype=int)
for i in range(size(cor)):
	if(cor[i]=='P'):
		cont[0] = cont[0] + 1
	elif(cor[i]=='C'):
		cont[1] = cont[1] + 1
	elif(cor[i]=='R'):
		cont[2] = cont[2] + 1
	elif(cor[i]=='L'):
		cont[3] = cont[3] + 1
	if(cor[i]=='B'):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)