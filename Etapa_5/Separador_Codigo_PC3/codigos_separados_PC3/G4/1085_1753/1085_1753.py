av1=float(input("informe nota da primeira avaliacao:"))
av2=float(input("informe nota da segunda avaliacao:"))
av3=float(input("informe nota da terceira avaliacao:"))
av4=float(input("informe nota da quarta avaliacao:"))
av5=float(input("informe nota da quinta avaliacao:"))
media=(av1+av2+av3+av4+av5)/5
if(media >=6):
	print(round(media, 2))
	print("Aprovado")
else:
	print(round(media, 2))
	print("Reprovado")
	