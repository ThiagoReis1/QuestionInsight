# faça seu código aqui!
n = int(input("Numero : "))
x = 0
y = 0
acm = 0
cont = 0
while x < n :
	x = x + 1
	y = x ** 3
	acm = y
	cont = cont + acm
print("soma=",cont)