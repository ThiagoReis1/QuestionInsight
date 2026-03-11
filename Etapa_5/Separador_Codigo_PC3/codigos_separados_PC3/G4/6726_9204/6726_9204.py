x = int(input("inserir um numero:"))

if x% 29 == 0:
	soma = x // 29
	print(soma)
	print("sim")
else:
	soma = x % 29
	print(soma)
	print("nao")