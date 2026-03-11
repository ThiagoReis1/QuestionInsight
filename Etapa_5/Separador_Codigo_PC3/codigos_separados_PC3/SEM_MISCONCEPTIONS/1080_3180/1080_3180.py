prova1=float(input("insira a nota da prova 1"))
prova2=float(input("insira a nota da prova 2"))
prova3=float(input("insira a nota da prova 3"))
media=(prova1+prova2+prova3)/3
print(round(media,1))
if(media>=5):
	print("Aprovado")
else:
	print("Reprovado")