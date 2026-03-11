prova1 = float(input("insira a nota da prova: "))
prova2 = float(input("insira a nota da prova: "))
prova3 = float(input("insira a nota da prova: "))
prova4 = float(input("insira a nota da prova: "))
prova5 = float(input("insira a nota da prova: "))
mediadasprovas = ((prova1 + prova2 + prova3 + prova4 + prova5)/5)
print(mediadasprovas)
if(mediadasprovas >=6): 
	print("Aprovado")   
else:
	print("Reprovado")