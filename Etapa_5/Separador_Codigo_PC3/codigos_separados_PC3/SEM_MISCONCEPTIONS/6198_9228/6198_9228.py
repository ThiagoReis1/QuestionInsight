altura_luna = 1.65
taxa_luna = 0.02
cont = 0
h = float(input("altura"))
t = float(input("taxa de crescimento"))

while h < altura_luna:
	
	cont = cont + 1
	
	h = h + t
	altura_luna = altura_luna + taxa_luna

print(cont)