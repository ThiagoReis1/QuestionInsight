from numpy import*

nota = eval(input("notas:"))
mf = (nota[0]*1.0 + nota[1]*2 + nota[2]*3 + nota[3]*4)/ 10.0
print (round(mf, 2))

if (mf >= 5.0):
	print ("APROVADO")
else:
	print ("REPROVADO")