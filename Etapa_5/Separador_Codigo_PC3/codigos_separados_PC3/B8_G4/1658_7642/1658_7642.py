from numpy import*
pais = input( ).upper().split(',')
#pais = pais_origem.split(',')
#cp = [0,0,0,0,0]
cp = zeros(5,dtype=int)
for x in pais:
	#pais = pais.upper()
	if x == 'CHN':
		cp[0] += 1
	elif x == 'JPN':
		cp[1] += 1
	elif x == 'KOR':
		cp[2] += 1
	elif x == 'MGL':
		cp[3] += 1
	elif x == 'THA':
		cp[4] +=1
m = max(cp)
print(m)
print(cp)