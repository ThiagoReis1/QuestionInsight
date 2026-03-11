from numpy import*
cont=zeros(4, dtype= int)
jogador=input().upper().split(",")
for v in jogador:
	if v == 'A':
		cont[0]+=1
	if v=='B':
		cont[1]+=1
	if v == 'C':
		cont[2]+=1
	if v == 'D':
		cont[3]+=1
print(cont)