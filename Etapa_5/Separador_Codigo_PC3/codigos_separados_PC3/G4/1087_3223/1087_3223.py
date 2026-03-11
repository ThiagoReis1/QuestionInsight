p1= float(input())
p2= float(input())
p3= float (input())
p4 =float (input())

med = (p1 + p2 + p3 + p4)/4

nota = (round(med, 2))

if (nota >= 7.0):
	mensagem = "Aprovado"
	
else:
	mensagem = "Reprovado"
print (nota)	
print (mensagem)