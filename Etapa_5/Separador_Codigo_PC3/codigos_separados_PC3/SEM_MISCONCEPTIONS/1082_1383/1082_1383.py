nota1 = float(input("Digite a nota da prova 01"))
nota2 = float(input("Digite a nota da prova 02"))
nota3 = float(input("Digite a nota da prova 03"))
nota4 = float(input("Digite a nota da prova 04"))
nota5 = float(input("Digite a nota da prova 05"))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5 

print (round(media, 1))
if (media >=5):
   print ("Aprovado")
else:  
   print ("Reprovado")

  