n = input()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if((n == "ASPARAGINA") or (n == "GLUTAMINA") or (n == "TRIPTOFANO")):
	if(n == "ASPARAGINA"):
		a = (C*4) + (H*8) + (N*2) + (O*3)
		print(round(a, 2))
	elif(n == "GLUTAMINA"):
		a = (C*5) + (H*8) + (N*1) + (O*4)
		print(round(a, 2))
	elif(n == "TRIPTOFANO")	:
		a = (C*11) + (H*11) + (N*2) + (O*2)
		print(round(a, 2))
	else:
		print("Entrada:", n)
		print("Dado Invalido")
else:
	print("Entrada:", n)
	print("Dado Invalido")