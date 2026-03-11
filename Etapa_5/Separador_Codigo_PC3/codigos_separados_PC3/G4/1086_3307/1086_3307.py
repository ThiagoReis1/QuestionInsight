n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 +  n2 + n3)/ 3

if (media >= 7):
	print(round(media, 1))
	print('Aprovado')
	
else: 
	print(round(media, 1))
	print('Reprovado')
	