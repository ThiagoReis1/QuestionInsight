a = input(" ")

i = 0
if(a.upper() != "S"):
	if(a.upper() == "A"):
		i = 1
while(a.upper() != "S"):
	a = input(" ")
	if(a.upper() == "A"):
		i = i + 1
print(i)



