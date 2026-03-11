qi = int(input( ))
d1 = int(input( ))
d2 = int(input( ))
d3 = int(input( ))

n = d1+d2+d3

pv = qi-10*n

if(pv>0):
	msg1 = pv
	msg2 = "Vivo"
else: 
	msg1 = 0
	msg2 = "Morto"
	
print(int(msg1))
print(msg2.upper())