f = input("Coxinha ou esfirra? ").upper()
q = int(input("Quantidade: "))
s = int(input("Quantidade de suco: "))

c = 2 * q
e = 4.5 * q
d = 6 * s

if (f == "C"):
	o = c + d
	print(round(o, 2))
else:
	k = e + d
	print(round(k, 2))