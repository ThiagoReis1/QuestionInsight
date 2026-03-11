x = int(input("digite o numero: "))
qct = x // 37
rest = x % 37
if x % 37 ==0 :
	print(qct)
	print("sim")
else:
	print(rest)
	print("nao")