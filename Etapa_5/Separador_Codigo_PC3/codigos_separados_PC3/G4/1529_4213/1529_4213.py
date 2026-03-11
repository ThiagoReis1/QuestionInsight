Inf1=int(input("Infinicial:"))
Cav1=int(input("Cavinicial:"))
Perinf=float(input("Percentual da Cavalaria:"))
Percav=float(input("Percentual da Infantaria:"))
P1=(Perinf/100)+1
P2=(Percav/100)+1
Mes=0
while((Inf1+Cav1)<50000):
	Inf1=Inf1*P1
	Cav1=Cav1*P2
	Mes=Mes+1
print(Mes)