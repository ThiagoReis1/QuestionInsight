notas1 = float(input())
notas2 = float(input())
notas3 = float(input())
notas4 = float(input())
notas5 = float(input())

media = (notas1 + notas2 + notas3 + notas4 + notas5)/5 
print(round(media,2))
if(media >= 7 ):
	mensagem =  "Aprovacao"
	print(mensagem)
else:
	mensagem = "Reprovacao por nota"
	print(mensagem)