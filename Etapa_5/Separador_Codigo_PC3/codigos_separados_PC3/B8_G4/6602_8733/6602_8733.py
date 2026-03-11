num = int(input("Alunos (votos): "))

c = 0
cp = 0
cl = 0
cc = 0

while c < num:
	l = input("letra: ").upper()
	if l == "L":
		c = c + 1
		cl = cl + 1
	elif l == "C":
		c = c + 1
		cc = cc + 1
	elif l == "P":
		c = c + 1
		cp = cp + 1
print("L=",cl)
print("C=",cc)
print("P=",cp)
