a = float(input("digite a media 1: "))
b = float(input("digite a media 2: "))
c = float(input("Digite a media 3: "))
d = float(input("Digite a media 4: "))
e = float(input("Digite a media 5: "))
media = ( a + b + c + d + e) / 5
print(round(media, 2))
if( media >= 6 ):
	print("Aprovado")
else:
	print("Reprovado")