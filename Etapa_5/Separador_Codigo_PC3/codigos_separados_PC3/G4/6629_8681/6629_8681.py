s = input("").upper()
i = 0
j = 0 
while i < len(s):
	if s[i]=="P":
		print(i)
		j = j + 1
	i = i + 1
if j == 0:
	print("nao achei")

	
	
	