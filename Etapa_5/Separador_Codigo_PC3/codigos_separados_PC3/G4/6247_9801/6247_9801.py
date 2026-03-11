A = input("Aluno? ICE/FT/ICOMP/X ") .upper()

c = 0

while A != "X":
	if A == "FT":
		c = c + 1
	A = input("Aluno? ICE/FT/ICOMP/X ")
print(c)