satisfacao = input("(S) satisfeito, (I)insatisfeitos, (N) neutro ").upper()

cont = 0
S = 0

while satisfacao != "X":
	if satisfacao =="S":
		S += 1
	satisfacao = input("(S) satisfacao, (I)insatisfeitos, (N) neutro ").upper()
	
print(S)
