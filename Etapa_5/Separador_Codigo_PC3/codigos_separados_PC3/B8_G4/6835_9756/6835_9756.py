prd = str (input("Que produto deseja, (B)Biscoitos; (C)Cereais; (E)Enlatados: ")).upper()
i = 0
cb = 0
cc = 0 
ce = 0
while i < len(prd):
	if prd[i] == 'B':
		cb = cb + 1 
	elif prd[i] == 'C':
		cc = cc + 1
	elif prd[i] == 'E':
		ce = ce + 1
	i = i + 1

vtc = (cb*3.75 + cc*7.90 + ce*9.85)

print (round(vtc, 2))