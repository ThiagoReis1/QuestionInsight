an= int(input('inserir ano de nascimento:'))
p= input('qual pais? (B/J):').upper()
idade= 2023-an

if p== 'B' and (idade>=21):
	print('sim')
	x= idade-21
	print(x)
elif p=='B' and (idade<21):
	print('nao')
	y= 21-idade
	print(y)
elif p=='J' and (idade>=20):
	print('sim')
	a= idade - 20
	print(a)
elif p=='J' and (idade<20):
	print('nao')
	b= 20 - idade
	print(b)
else:
	print('invalido')
