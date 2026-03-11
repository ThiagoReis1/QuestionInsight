s = input("Escreva a palavra que voce quiser: ").upper()

custo = 0

i = 0

while (i < len(s)):
	if (s[i] == "A"):
		custo = custo + 0.19
	if (s[i] == "E"):
		custo = custo + 0.19
	if (s[i] == "I"):
		custo = custo + 0.19
	if (s[i] == "O"):
		custo = custo + 0.19
	if (s[i] == "U"):
		custo = custo + 0.19
	if (s[i] != "A" and s[i] != "E" and s[i] != "I" and s[i] != "O" and s[i] != "U"):
		custo = custo + 0.23
	i = i + 1

print(round(custo, 2))