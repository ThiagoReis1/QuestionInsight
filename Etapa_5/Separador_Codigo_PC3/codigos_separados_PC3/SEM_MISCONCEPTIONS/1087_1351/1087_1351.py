nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota: "))
nota4 = float(input("informe a quarta nota: "))
media = ((nota1+nota2+nota3+nota4) / 4)
print(round(media,2))
if (media) >= 7.00 :
	print("Aprovado")
else:
	print("Reprovado")