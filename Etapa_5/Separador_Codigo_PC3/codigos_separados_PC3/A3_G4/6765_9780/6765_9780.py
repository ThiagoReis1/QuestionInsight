ano = int(input("ano de nascimento: "))
pais=input("(B) brasil and (R) russia").upper()

idade = 2023 - ano

if pais == 'B' and idade >= 18:
	print('sim')
	f=idade-18
	print(f)
elif pais == 'B' and idade < 18:
	print('nao')
	x=18-idade
	print(x)
elif pais == 'R' and idade >= 21:
	print('sim')
	y=idade-21
	print(y)
elif pais < 'R' and idade < 21:
	print('nao')
	z=21-idade
	print(y)
else:
	print("invalido")
