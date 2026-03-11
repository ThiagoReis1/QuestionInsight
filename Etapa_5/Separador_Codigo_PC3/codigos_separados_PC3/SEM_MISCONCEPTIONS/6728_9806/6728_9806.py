n = int(input("Numero: "))
conta = n // 37
if n % 37 == 0 :
	print(conta)
	print("sim")
else: 
	print(n % 37)
	print("nao")