a = float(input("prova a :"))
b = float(input("prova b :"))
c = float(input("prova c: "))
d = float(input("prova d: "))

f = (a + b + c + d) /4

if (f >= 7.0 ):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
	
print(round(f,2))
print(mensagem)

