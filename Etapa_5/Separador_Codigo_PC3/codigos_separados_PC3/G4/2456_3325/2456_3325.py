x = float(input("valor da mensalidade: "))
y = int(input("numero de pirralho: "))
if(y>0):
	if(y==1):
		vt = x-(x*0.1)
		print(vt)
	elif(y==2):
		vt = y*(x-(x*0.3))
		print(vt)
	else:
		vt = y*(x-(x*0.4))
		print(vt)