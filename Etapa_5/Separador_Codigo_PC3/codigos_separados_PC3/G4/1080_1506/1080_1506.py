n1=float(input("digite a primeira nota:"))
n2=float(input("digite a primeira nota:"))
n3=float(input("digite a primeira nota:"))
media=((n1+n2+n3)/3)
if(media>=5):
	print(round(media,1))
	print("Aprovado")
else:
	print(round(media,1))
	print("Reprovado")
	