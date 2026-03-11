#notas
nota1=float(input("nota1:"))
nota2=float(input("nota2:"))
nota3=float(input("nota3:"))
# media
media=(nota1+nota2+nota3)/3
print(round(media,2))

if(media>=6.0):
	print("Aprovacao")
else:
	print("Reprovacao")