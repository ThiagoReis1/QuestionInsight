a = float(input(''))
b = float(input(''))
c = float(input(''))
d = float(input(''))
e = float(input(''))

me = round((a + b + c + d + e)/ 5, 1)

if me >= 5.0:
	print(me)
	print('Aprovado')
else:
	print(me)
	print('Reprovado')