nota1 = float(input("digite:"))
nota2 = float(input("digite:"))
nota3 = float(input("digite:"))
nota4 = float(input("digite:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

media_arredondada = round(media, 1)

if media >= 6.0:
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
	
print(media_arredondada)
print(mensagem)