i = int(input("Digite a idade: "))

x = 0
a = 0

while i != -1:
	i = int(input("Digite a idade: "))
	if i < 18 and i != -1:
		a = a + 1
	x = x + 1
print(x)
print(a)
y = (a*100)/x
print(round(y,2))