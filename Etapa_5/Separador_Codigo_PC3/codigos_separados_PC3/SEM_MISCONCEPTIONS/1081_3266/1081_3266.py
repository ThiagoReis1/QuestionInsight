nota1= float(input("Valor da media 1:"))
nota2= float(input("Valor da media 2:"))
nota3= float(input("Valor da media 3:"))
nota4= float(input("Valor da media 4:"))

media=(nota1+nota2+nota3+nota4)/4

if(media>=5):
   mensagem=("Aprovacao")
else:
	mensagem=("Reprovacao")
print(round(media, 2))
print(mensagem)
	