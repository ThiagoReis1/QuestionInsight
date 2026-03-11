u1=(input("unidade:"))
u2= float(input("valor:"))
if u1=="K":
	mi= u2/1.60934
	print (round((mi),2))
else:
	km=1.60934*u2
	print(round((km),2))

