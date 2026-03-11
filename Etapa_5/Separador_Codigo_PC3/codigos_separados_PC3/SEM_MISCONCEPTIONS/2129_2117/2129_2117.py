from numpy import*
nota=array(eval(input("digite as notas: ")))

Mfinal=((nota[0])*1+(nota[1])*2+(nota[2])*3+(nota[3])*4)/10.0
print(round(Mfinal,2))

if(Mfinal>=5.0):
	print("APROVADO")
else:
	print("REPROVADO")