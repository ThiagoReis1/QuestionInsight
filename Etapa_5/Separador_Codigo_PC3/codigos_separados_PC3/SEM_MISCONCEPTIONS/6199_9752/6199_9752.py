
altura_cicero = 1.8
taxa_cicero = 0.01

a = float(input("qual a altura: "))
b = float(input("qual a taxa: "))

cont = 0

while  (a <= altura_cicero):
	cont = cont + 1
	a = a + b
	altura_cicero = altura_cicero + taxa_cicero
	
print(cont)
