p1 = float(input("Qual e a nota?"))
p2 = float(input("Qual e a nota?"))
p3 = float(input("Qual e a nota?"))

media = p1 + p2 + p3 / 3

if (media >= 6): 
	mensagem = "aprovado"
else:
	mensagem = "reprovado"
	
print(round(media, 2))
print(aprovacao)
