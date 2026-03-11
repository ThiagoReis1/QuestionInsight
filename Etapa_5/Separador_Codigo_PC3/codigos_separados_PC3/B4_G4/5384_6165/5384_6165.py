a = input("").upper()

i = 0
j = 0

while(i < len(a)):
	if(a[i] == "A"):
		j = j + 45.15
	elif(a[i] == "E"):
		j = j + 45.15
	elif(a[i] == "I"):
		j = j + 45.15
	elif(a[i] == "O"):
		j = j + 45.15
	elif(a[i] == "U"):
		j = j + 45.15
	else:
		j = j + 50.17
	i = i + 1
print(round(j, 2))