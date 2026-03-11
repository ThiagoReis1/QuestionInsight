altura_cicero = 1.8
taxa_cicero = 0.01

f = float(input("vai: "))
t = float(input("agora: "))

a = 0

while (f <= altura_cicero):
	altura_cicero += taxa_cicero
	f += t
	a += 1
	
print(a)