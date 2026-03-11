#NOTAS
nota1 = float(input("Digite a nota da prova 1: ")) 
nota2 = float(input("Digite a nota da prova 2: ")) 
nota3 = float(input("Digite a nota da prova 3: ")) 
nota4 = float(input("Digite a nota da prova 4: ")) 
nota5 = float(input("Digite a nota da prova 5: ")) 

#MEDIA
media = (nota1 + nota2 + nota3 + nota4 + nota5)/ 5
print(round(media, 2))

if(media >= 7.0):
	print("Aprovacao")
else:
	print("Reprovacao por nota")