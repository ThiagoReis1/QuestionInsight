a = int(input("digite o ano: "))
b = input("digite o pais: ").upper()

c = 2023 -a

if b == "B" and c >= 21:
	print("sim")
	f = c -21
	print(f)
elif b == "B" and c < 21:
	print("nao")
	f = 21 - c
	print(f)
elif b == "R" and c >= 18:
	print("sim")
	f = c -18
	print(f)
elif b == "R" and c <= 18:
	f = 18 - c
	print("nao")
	
else :
	print("invalido")
	
	

	