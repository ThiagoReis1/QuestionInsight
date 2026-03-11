nota1 = float (input ("informe a primeira nota: "))
nota2 = float (input ("informe a segunda nota: "))
nota3 = float (input ("informe a terceira nota: "))
nota4 = float (input ("informe a quarta nota: "))

x = (nota1 + nota2 + nota3 + nota4) / 4
print (round (x , 1))

if	(x >= 6.0):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
	
print (mensagem)