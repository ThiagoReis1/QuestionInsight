n = input()

cara = 0
coroa = 0
j = 1

while (n.upper() != "S"):
	if (n.upper() == "CARA"):
		cara = cara + 1
	else:
		coroa = coroa + 1
	n = input()

j = cara + coroa
fc = (100 * cara)/j

print(j)
print(round(fc, 2))