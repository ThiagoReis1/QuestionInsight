inf = int(input(""))
cav = int(input(""))
crescInf = float(input(""))
crescCav = float(input(""))

tempo = 0

while((inf+cav) < 50000):
	inf *= (crescInf+100)/100
	cav *= (crescCav+100)/100
	
	tempo += 1

print(tempo)
