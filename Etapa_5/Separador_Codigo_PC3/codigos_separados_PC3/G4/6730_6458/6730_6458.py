x =  int(input("diga um numero: "))

if x % 43 == 0:
	di = x // 43
	print(di)
	print("sim")
else:
	di = x % 43
	print(di)
	print("nao")
	