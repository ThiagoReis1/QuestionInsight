rest = input("Resultado da partida V/E/D: ").upper()
pont = 0
cont = 0

while rest != "X":
	if rest == "V":
		pont = pont + 3
	elif rest == "E":
		pont = pont + 1
	elif rest == "D":
		pont == pont + 0
	rest = input("Resultado: ").upper()	
	cont = cont + 1

p = (pont/cont*3)*100

print(p)
	
	
	