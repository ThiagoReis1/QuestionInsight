nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))

media = (nota1 + nota2 + nota3)/3

if (media >= 7):
    mensagem = ("Aprovado")
else:
	 mensagem = ("Reprovado")

print(round(media, 1))
print(mensagem)
		
	 