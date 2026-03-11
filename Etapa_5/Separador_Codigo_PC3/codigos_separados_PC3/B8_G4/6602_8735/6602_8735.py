# faça seu código aqui!
N = int(input("Digite o numero de integrantes: "))
c = 0

acmL= 0
acmC= 0
acmP= 0

while (c < N):
	g = input("digite a letra: ").upper()
	if (g == "L"):
		acmL = acmL + 1
	elif (g == "C"):
		acmC = acmC + 1
	elif (g == "P"):
		acmP = acmP + 1
	c = c + 1

print("L= ", acmL)
print("C= ", acmC)
print("P= ", acmP)