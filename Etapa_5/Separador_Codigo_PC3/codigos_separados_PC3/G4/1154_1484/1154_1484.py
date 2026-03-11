virus = int(input("n° de copias do virus : "))
taxa = int(input("taxa de redução: "))
ent = int(input("n° entrada de novas copias: "))
sema = 0

while(virus < 1*10**6):
	virus = virus- (taxa*virus)/100
	virus = virus + ent
	sema =  sema + 1
print (sema)