a = int(input("Idade do entrevistado: "))
m = 0

while (a != -1):
	if (a < 18):
		m = m + 1
	else:
		m = m
	a = int(input("Idade do entrevistado: "))
print(m)