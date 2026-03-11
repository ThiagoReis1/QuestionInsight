a = input("Digite (S) se estiver satisfeito (I) se estiver insatisfeito, (N) caso nao queira opinar ou (X) para encerrar o programa:").upper()
s = 0
while a != "X":
	if a == "S":
		s += 1
		a= input("De novo")
	elif a== "I" or "N":
		a= input("De novo")
print(s)