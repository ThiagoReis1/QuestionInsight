av1=float(input("Informe nota da primeira avaliacao:"))
av2=float(input("Informe nota da segunda avaliacao:"))
av3=float(input("Informe nota da terceira avaliacao:"))
av4=float(input("Informe nota da quarta avaliacao:"))
media=(av1+av2+av3+av4)/4
if(media>=7):
	print(round(media, 2))
	print("Aprovado")
else:
	print(round(media, 2))
	print("Reprovado")