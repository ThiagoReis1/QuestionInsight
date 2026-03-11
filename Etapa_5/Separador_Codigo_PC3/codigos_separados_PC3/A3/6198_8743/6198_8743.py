altura_luna = 1.65
taxa_luna = 0.02
a = float(input("Digite sua altura: "))
t = float(input("Digite a taxa: "))
c = 0
ac = 0

while (a < altura_luna):
		altura_luna = altura_luna + taxa_luna
		a = a + t
		c = c + 1
print(c)