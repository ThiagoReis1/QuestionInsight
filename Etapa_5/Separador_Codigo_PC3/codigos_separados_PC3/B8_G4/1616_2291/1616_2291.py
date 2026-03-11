from numpy import*
v = array(input(""))
n = array(eval(input("")))

i = 0
k = 0

while ( k < size(n)):
	if ( v[k] == "GELO"):
		g = 2 * n[i]
		i = i + 1
		k = k + 1
		
	elif ( v[k] == "FOGO"):
		f = 3 * n[i]
		i = i + 1
		k = k + 1
		
	elif ( v[k] == "CHOQUE"):
		c = 4 * n[i]
		i = i + 1
		k = k + 1
		
	elif ( v[k] == "CONJURACAO"):
		co = 8 * n[i]	
		i = i + 1
		k = k + 1
		
	elif ( v[k] == "ILUSAO"):
		il = 10 * n[i]	
		i = i + 1
		k = k + 1
		
danot = g + f + c + co + il
print(danot)