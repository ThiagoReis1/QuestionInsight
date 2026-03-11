from numpy import*

vt = array(eval(input('tempo: ')))

mx = max(vt)

posição = 0

for i in vt:
	if ( i == mx ):
		print(posição)
	else:
		posição = posição + 1
	
	

