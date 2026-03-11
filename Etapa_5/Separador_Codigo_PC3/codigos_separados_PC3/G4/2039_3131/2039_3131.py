s = input("nucleotideo 1: ")

num = 0

while (s.upper() != "S"):
	if (s.upper() == "A"):
		num = num + 1
	else:
		s = input("nucleotideo seguinte: ")

print(num)