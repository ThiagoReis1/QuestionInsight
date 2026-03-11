nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
nota3 = float(input("Insira sua terceira nota: "))
nota4 = float(input("Insira sua quarta nota: "))
media =(nota1+nota2+nota3+nota4)/4
print (round(media,1))
if (media>=6 ):
	print("Aprovado")
else: 
	print("Reprovado")