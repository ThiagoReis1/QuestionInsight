an = int(input("ano de naisxcimento: "))
pa = input("pais p ve: ").upper()

cc = 2023 - an
vr = cc - 18
vj = cc - 16
vb = 18 - cc
vt = 16 - cc

if pa != "B" and  pa != "J":
	print("invalido")
elif cc >= 18 and pa == "B":
	print("sim")
	print(vr)
elif cc < 18 and pa == "B":
	print("nao")
	print(vb)
elif cc >= 16 and pa == "J":
	print("sim")
	print(vj)
elif cc < 16 and pa == "J":
	print("nao")
	print(vt)