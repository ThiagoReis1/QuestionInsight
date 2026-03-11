altura_cicero = 1.75
taxa_cicero = 0.01
x=float(input("Altura: "))
y=float(input("Taxa de crescimento: "))
anos = 0
while altura_cicero > x :
	altura_cicero += taxa_cicero
	x += y
	anos += 1
print(anos)