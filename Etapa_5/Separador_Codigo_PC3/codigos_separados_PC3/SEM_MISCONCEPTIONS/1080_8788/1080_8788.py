nota_x = float(input('insira a primeira nota:'))
nota_y = float(input('insira a segunda nota:'))
nota_z = float(input('insira a terceira nota:'))

media = round(((nota_x + nota_y + nota_z) / 3),1)

if media >= 5:
	print(round(media,2))
	print('Aprovado')
else:
	print(round(media,2))
	print('Reprovado')


