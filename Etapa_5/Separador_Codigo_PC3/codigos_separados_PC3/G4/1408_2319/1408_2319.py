arma = input()
d = int(input("Digite a destreza aqui: "))
D1 = int(input("Digite D1 aqui: "))
D2 = int(input("Digite D2 aqui: "))
s = D1+D2
if (arma == "katana"):
	dk= 2*s + d
	print(dk)
else:
	ds= s + 2*d
	print(ds)