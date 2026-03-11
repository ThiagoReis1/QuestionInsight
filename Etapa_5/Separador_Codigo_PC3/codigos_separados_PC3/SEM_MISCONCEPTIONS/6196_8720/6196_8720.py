alturachico = 1.5
taxachico = 0.02
alturaaluno=float(input())
taxaaluno=float(input())
cont=0
while(alturaaluno<alturachico):
	alturaaluno=alturaaluno+taxaaluno
	alturachico=alturachico+taxachico
	cont=cont+1
print(cont)