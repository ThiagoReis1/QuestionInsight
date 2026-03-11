from numpy import*

v1 = array(eval(input()))
v2 = array(eval(input()))

i = 0
p = 0
p2 = 0
p3 = 0
p4 = 0

r = 0
r2 = 0 
r3 = 0
r4 = 0
while i < size(v1):
	if v1[i] == 1:
		p = p + 40
	elif v1[i] == 2:
		p2 = p2 + 20
	elif v1[i] == 3:
		p3 = p3 + 10
	else:
		p4 = p4 + 0
	
	if v2[i] == 1:
		r = r + 40
	elif v2[i] == 2:
		r2 = r2 + 20
	elif v2[i] == 3:
		r3 = r3 + 10
	else:
		r4 = r4 + 0  
	i = i + 1	

if (p + p2 + p3 + p4) > (r + r2 + r3 + r4):
	print("JOGADOR UM")
elif (p + p2 + p3 + p4) == (r + r2 + r3 + r4):
	print("EMPATE")
else:
	print("JOGADOR DOIS")
		