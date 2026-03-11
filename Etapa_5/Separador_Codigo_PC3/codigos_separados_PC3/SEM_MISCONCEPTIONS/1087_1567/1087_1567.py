nota1= float(input ("digite a primeira nota"))
nota2= float(input ("digite a segunda nota"))
nota3= float (input ("digite a terceira nota"))
nota4= float(input ("digite a quarta nota"))

media_notas= (nota1+nota2+nota3+nota4)/4

print (round (media_notas,2))
	
if media_notas >= 7:
	print("Aprovado")
	
else:
	
	print ("Reprovado")
	