n1 = float(input("Informe a primeira de Chilperico: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))
media = float((n1+n2+n3+n4)/4)
media2 = round(media,2)
print (media2)
if (media2 >= 7):
	print ("Aprovado")
else:
	print ("Reprovado")