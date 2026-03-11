from numpy import*


v = input("pais: ").upper().split(',')
vc = array([0,0,0,0,0])
for tipo in v:
	if tipo == 'CHN':
		vc[0]=vc[0]+1
	elif tipo == 'JPN':
		vc[1]=vc[1]+1
	elif tipo == 'KOR':
		vc[2]=vc[2]+1
	elif tipo == 'MGL':
		vc[3]=vc[3]+1
	elif tipo == 'THA':
		vc[4]=vc[4]+1
print(max(vc))
print(vc)

