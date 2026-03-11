a = input("insira o rotulo:")
i = 0
s = 0
while(i<len(a)):
	if(a[i] == "A") or(a[i] == "E") or (a[i] == "I") or (a[i] == "O") or (a[i] == "U"):
		s = s + 0.25
	else:
		s = s + 0.27
	i = i + 1
print(round(s, 2))
		