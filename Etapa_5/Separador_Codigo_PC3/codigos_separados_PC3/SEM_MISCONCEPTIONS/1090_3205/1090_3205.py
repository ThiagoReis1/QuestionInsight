limite= float(input())
compra1= float(input())
compra2= float(input())
compra3= float(input())
compra4= float(input())
total= compra1 + compra2 + compra3 + compra4
print(round(total,2))
if (total <= limite):
	mensagem= "Dentro do limite"
else:
	mensagem= "Estourou o limite"
print(mensagem)