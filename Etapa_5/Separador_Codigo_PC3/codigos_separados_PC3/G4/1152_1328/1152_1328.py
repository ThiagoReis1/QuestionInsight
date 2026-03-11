nb=int(input("Habitantes de Bravos:"))
np=int(input("Habitantes de Pentos:"))
npr=int(input("Habitantes de Porto real:"))
cb=float(input("Crescimento da População de Bravos?:"))/100
cp=float(input("Crescimento da População de Pentos?:"))/100
cpr=float(input("Crescimento da População de Porto Real?:"))/100
ano=1
while nb==np==npr:
	nb+=nb*cb
	np+=np*cp
	npr+=npr*cpr
	ano+=1
print(ano)