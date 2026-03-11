altura_cicero = 1.8
taxa_cicero = 0.01
h = float(input("altura: "))
t = float(input("taxa: "))
cont = 0
while(h <= altura_cicero):
	cont = cont + 1
	h = h + t
	altura_cicero = altura_cicero + taxa_cicero
print(cont)
	