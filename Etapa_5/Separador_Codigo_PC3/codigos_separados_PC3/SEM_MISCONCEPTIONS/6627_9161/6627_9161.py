string = input(" palavra : ").upper()
i = 0
cont = 0
while i < len(string) :
	if string[i] == "D" :
		cont += 1
	i += 1
print(cont)