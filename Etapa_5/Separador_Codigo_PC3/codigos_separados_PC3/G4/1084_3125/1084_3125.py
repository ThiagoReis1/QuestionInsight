a = float(input("resultado da prova a:"))
b = float(input("resultado da prova b:"))
c = float(input("resultado da prova c:"))
d = float(input("resultado da prova d:"))

f = (a + b + c + d) / 4

if (f >= 6.0):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
   
print (round(f,1))
print (mensagem)