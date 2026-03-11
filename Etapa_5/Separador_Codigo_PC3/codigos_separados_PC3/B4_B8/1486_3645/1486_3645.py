nome = input().upper()
quantidade = int(input())
if( quantidade < 0 or quantidade > 10000):
	print("Entrada invalida")
elif(nome == 'ARROZ'):
	x = quantidade // 500
	print(x)
elif(nome == 'CENOURA'):
	x = quantidade // 100
	print(x)
elif(nome == 'KAMPYO'):
	x = quantidade // 20
	print(x)
elif(nome == 'NORI'):
	x = quantidade // 50
	print(x)
elif(nome == 'OMELETE'):
	x = quantidade // 200
	print(x)
elif(nome == 'PEPINO'):
	x = quantidade // 150
	print(x)
elif(nome == 'SALMAO'):
	x = quantidade // 300
	print(x)
elif(nome == 'SHITAKE'):
	x = quantidade // 150
	print(x)