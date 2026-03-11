tam = int(input("digite quantidade de tambaquis:"))
pac = int(input("digite quantidade de pacus:"))
tt = float(input("taxa de crescimento tam:"))
tp = float(input("taxa de crescimento pac:"))
v = int(input("total do viveiro:"))

anos = 1
peixes = 0


while (peixes <= v):
				tam = tam * (1 + (tt / 100))
				pac = pac * (1 + (tp / 100))
				anos = anos + 1
				peixes = peixes +tam + pac
		
else:		
				print(anos)
