x = int(input("Insira um Numero Inteiro X: "))

if x % 29 == 0:
	print( x // 29 )
	print("sim")
else:
	print( x % 29 )
	print("nao")