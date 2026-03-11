res = input("vitoria ou empate de qual time? ").upper()

S = 0

while res != "X":
	if res == "A":
		S = S + 1
	res = input("vitoria ou empate de qual de time? ").upper()
print(S)