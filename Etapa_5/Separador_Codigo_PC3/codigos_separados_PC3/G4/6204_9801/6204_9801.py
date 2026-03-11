AM = 1.86
TCM = 0.01

c = 0

AC = float(input("Altura do coelho: "))
TCC = float(input("Taxa de crescimento do coelho: "))

while AC < AM:
	AM = AM + TCM
	AC = AC + TCC
	c = c + 1
print(c)