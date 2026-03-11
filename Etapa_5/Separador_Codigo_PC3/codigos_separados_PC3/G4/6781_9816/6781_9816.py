ano = int(input('Digite o ano de nascimento:'))
p= input('Brasil(B) ou Estados Unidos(E)').upper()

c = 2023-ano

if p=='B':
	if c>=21:
		tempo= c-21
		print('sim')
		print(tempo)
	else:
		tempo=21-c
		print('nao')
		print(tempo)
elif p=='E':
	if c>=18:
		tempo= c-18
		print('sim')
		print(tempo)
	else:
		tempo=18-c
		print('nao')
		print(tempo)
else:
	print('invalido')