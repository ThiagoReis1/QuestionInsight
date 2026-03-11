a= int(input("ano de nascimento:"))
p = input("pais:"). upper()
c = 2023 - a
f= c - 18
b= c - 17
d = 18 - c
e = 17 - c
if p == "B":
	if c >= 18:
		print("sim")
		print(f)
	else:
		print("nao")
		print(d)
elif p == "R":
	if c >= 17:
		print("sim")
		print(b)
	else:
		print("nao")
		print(e)
else:
	print("invalido")