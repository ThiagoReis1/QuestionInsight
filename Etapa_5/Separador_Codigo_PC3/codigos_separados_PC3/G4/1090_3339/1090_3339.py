l = float(input("e"))
v1 = float(input("a"))
v2 = float(input("b"))
v3 = float(input("c"))
v4 = float(input("d"))

vt = (v1 + v2 + v3 + v4)
print(round(vt, 2))

if (vt <= l):
	mensagem = "Dentro do limite"
else:
	mensagem = "Estourou o limite"

print(mensagem)