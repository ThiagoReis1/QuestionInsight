n1=float(input("digite a primeira nota: "))
n2=float(input("digite a segunda nota: "))
n3=float(input("digite a terceira nota: "))

media = (n1+n2+n3)/3
media2=round(media,1)

if (media2 == 7.0 or media2 > 7.0):
	print(media2)
	print("Aprovado")
else:
	print(media2)
	print("Reprovado")
	
