nota1=float(input("digite a nota 1"))
nota2=float(input("digite a nota 2"))
nota3=float(input("digite a nota 3"))

m=(nota1+nota2+nota3)/3

if(m>=7):
	mensagem= "Aprovado"
	
else:
	mensagem= "Reprovado"
print(round(m,1))
print(mensagem)