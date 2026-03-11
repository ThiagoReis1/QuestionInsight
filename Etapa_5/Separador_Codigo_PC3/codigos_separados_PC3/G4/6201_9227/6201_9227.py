ajoe = 1.77
tjoe = 0.02
a = float(input("altura de uma pessoa:"))
t = float(input("taxa de crescimento:"))
cont = 0
while a < ajoe:
	cont = cont + 1
	a = a + t
	ajoe = ajoe + tjoe
print(cont)
	
