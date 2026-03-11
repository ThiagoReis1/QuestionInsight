s = input("").upper()
cont = 0
i = 0

while(i < len(s)):
	if(s[i] == "D"):
		cont = cont + 1
	i = i + 1
print(cont)
