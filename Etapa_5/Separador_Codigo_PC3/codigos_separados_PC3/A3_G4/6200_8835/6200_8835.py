ci = 1.75
cero = 0.01
al = float(input(""))
uno = float(input(""))
cont = 0
while al < ci:
	al = al + uno 
	ci = ci + 0.01
	cont += 1
print(cont)