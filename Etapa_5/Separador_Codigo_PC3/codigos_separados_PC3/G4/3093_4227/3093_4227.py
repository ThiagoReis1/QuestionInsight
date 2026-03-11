a = input("").upper()
i = 0
s = 0
while (a!="X"):
	if (a=="V"):
		i = i + 1 
	if (a=="E"):
		s = s + 1 
	a = input("").upper()
print(3*i)
print(s)