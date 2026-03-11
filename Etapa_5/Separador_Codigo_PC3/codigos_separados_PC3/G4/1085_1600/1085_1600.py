p1=float(input("nota prova 1:"))
p2=float(input("nota prova 2:"))
p3=float(input("nota prova 3:"))
p4=float(input("nota prova 4:"))
p5=float(input("nota prova 5:"))

media=(p1+p2+p3+p4+p5)/5
print(round(media, 2))
if (media>=6):
	mensagem="Aprovado"
else:
	mensagem="Reprovado"
print(mensagem)
