c = input('Digite T para tapioca ou S para salgado: ').upper()
q = int(input('Digite a quantidade de tapiocas ou salgados: '))
qa = int(input('Digite a quantidade de acais:'))

if c == 'T':
	total = 3.5 * q + qa * 13
else:
	total = 5 * q + qa * 13
	
print(round(total, 2))