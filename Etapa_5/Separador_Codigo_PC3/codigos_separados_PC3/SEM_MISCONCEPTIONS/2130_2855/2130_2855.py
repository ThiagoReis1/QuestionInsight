from numpy import*

v = eval(input("notas:"))

Mfinal = (v[0]*3 + v[1]*2 + v[2]*2 + v[3]*3)/10

if(Mfinal >= 5):
	print(round(Mfinal,2))
	print("APROVADO")
else:
	print(round(Mfinal,2))
	print("REPROVADO")