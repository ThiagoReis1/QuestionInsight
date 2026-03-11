altura_chico = 1.5
taxa_chico = 0.02
anos = 0
h = float(input("Altura: "))
t = float(input("Taxa de crescimento: "))

while (h < altura_chico):
	altura_chico += taxa_chico
	h += t
	anos = anos + 1
print(anos)
	