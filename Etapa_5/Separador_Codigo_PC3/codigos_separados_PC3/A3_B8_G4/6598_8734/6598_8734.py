qnts = int(input('quantos?'))
t = 0
e = 0
a = 0
cont = 0

while cont < qnts:
	qm = input('').upper()
	cont += 1
	
	if 0 == 'T': 
		t += 1
		
	elif 0 == 'E': 
		e += 1
		
	elif 0 == 'A': 
		a += 1
		
print('tais=',t)
print('edgar=',e)
print('ana=',a)