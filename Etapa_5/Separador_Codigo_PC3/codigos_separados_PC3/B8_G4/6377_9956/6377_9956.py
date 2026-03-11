from numpy import*
gol=input().upper().split(",")
aux= zeros(4,dtype=int)
for i in range(0,size(gol)):
	if gol[i]=='A':
		aux[0]= aux[0] + 1
	elif gol[i]=='B':
		aux[1]= aux[1] + 1
	elif gol[i]=='C':
		aux[2]= aux[2] + 1
	elif gol[i]=='D':
		aux[3]= aux[3] + 1
print(aux)
	
	