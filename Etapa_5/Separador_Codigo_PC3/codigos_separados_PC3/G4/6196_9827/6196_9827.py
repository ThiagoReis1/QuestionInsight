ac = 1.5
tc = 0.02
ap = float(input())
tp = float(input())
tempo = 0 
while	ap < ac:
	ap = ap + tp
	ac = ac + tc
	tempo = tempo + 1
print(tempo)