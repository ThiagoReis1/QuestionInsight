num=int(input())
pais=input()
pais=	pais.upper()
idade=2023-num
if pais=='B' and idade >= 18:
	print("sim")
	print(idade - 18)
elif pais == 'B' and idade < 18:
	print('nao')
	print(18 - idade)
elif pais == 'E' and idade >= 16:
	print('sim')
	print(idade - 16)
elif pais == 'E' and idade < 16:
	print('nao')
	print(16 - idade)
else:
	print("invalido")