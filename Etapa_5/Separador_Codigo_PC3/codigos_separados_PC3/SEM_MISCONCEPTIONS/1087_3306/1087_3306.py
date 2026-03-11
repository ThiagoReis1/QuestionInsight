#leitura das notas
nota1= float(input("digite o valor da nota1:"))
nota2= float(input("digite o valor da nota2:"))
nota3= float(input("digite o valor da nota3:"))
nota4= float(input("digite o valor da nota4:"))
#media aritmetica
media= (nota1+nota2+nota3+nota4)/4
print(round(media,2))
if(media>=7):
	mensagem= "Aprovado"
else:
	mensagem= "Reprovado"
print(mensagem)