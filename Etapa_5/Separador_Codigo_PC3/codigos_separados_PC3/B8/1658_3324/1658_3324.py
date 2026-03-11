from numpy import*

p= input()
vetor= p.split(',')

paises= zeros(5,dtype=int)

for i in vetor:
	if i=="CHN":
		paises[0]= paises[0]+1
	elif i=="JPN":
		paises[1]= paises[1]+1
	elif i=="KOR":
		paises[2]= paises[2]+1
	elif i=="MGL":
		paises[3]= paises[3]+1
	elif i=="THA":
		paises[4]= paises[4]+1

		
print(max(paises))
print(paises)


