T = 5.5
S = 4
A = 10

qual = input(" ")
qtd = int(input(" "))
acai = int(input(" "))

if(qual == "S"):
	final = (S * qtd) + (acai * A)
	print(final)
else:
	final = (T * qtd) + (acai * A)
	print(final)

