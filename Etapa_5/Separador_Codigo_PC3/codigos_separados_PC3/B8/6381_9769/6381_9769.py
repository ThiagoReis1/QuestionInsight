from numpy import*

cartas = input('').split(',')
naipe = zeros(4,dtype=int)
	
for v in cartas:
	if v =='C':
		naipe[0]+=1
	elif v =='O':
		naipe[1]+=1
	elif v =='P':
		naipe[2]+=1
	elif v =='E':
		naipe[3]+=1
print(naipe)