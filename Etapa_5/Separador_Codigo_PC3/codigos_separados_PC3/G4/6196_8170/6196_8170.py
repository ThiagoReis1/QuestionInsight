aC = 1.5
tC = 0.02

aP = float(input("Altura: "))
tP = float(input("Taxa de crescimento: "))

a = 0

while (aP<aC):
	aC = tC+aC
	aP = tP+aP
	a = a + 1
print(a)