x = int(input("Digite um numero inteiro: "))
a = x % 41

if a == 0:
	print (x // 41) 
	print("sim")
else:
	print(x % 41)
	print("nao")