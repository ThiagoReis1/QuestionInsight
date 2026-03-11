s = input("Digite uma palavra: ").upper()
i = 0
j = 0

while i < len(s):
	if s[i] == "L":
		print(i)
		j += 1
	i += 1
	
if j == 0:
	print("nao achei")
	