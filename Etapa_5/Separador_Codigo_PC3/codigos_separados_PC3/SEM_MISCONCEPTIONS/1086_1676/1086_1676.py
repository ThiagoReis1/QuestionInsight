nota1 = float(input("qual a nota1?"))
nota2 = float(input("qual a nota2?"))
nota3 = float(input("qual a nota3?"))
media = (nota1 + nota2 + nota3) / 3

if(media >= 7):
	print(round(media,1))
	print("Aprovado")			
	
else:	
	print(round(media,1))			
	print("Reprovado")