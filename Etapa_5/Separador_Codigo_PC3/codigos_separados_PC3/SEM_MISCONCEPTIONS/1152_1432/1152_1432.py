nbrav = int(input("Nro hab Bravos:"))
npen = int(input("Nro hab Pentos:"))
npreal = int(input("Nro hab Bravos:"))
tbrav = float(input("Tx Bravos:"))
tpen = float(input("TX Pentos:"))
tpreal = float(input("Tx Porto Real:"))
cont = 1 
while((nbrav + npen) < npreal):
	nbrav = nbrav * (1 + tbrav/100)
	npen = npen * (1 + tpen/100)
	npreal = npreal * (1 + tpreal/100)
	cont = cont + 1
print(cont)
	