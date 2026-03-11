from math import*
ppentos = float(input("População de Pentos: "))
pbravos = float(input("População de Bravos: "))
pportoreal = float(input("População de Porto Real: "))
tpentos = float(input("Taxa Pentos: "))
tbravos = float(input("Taxa Bravos: "))
tportoreal = float(input("Taxa Porto Real: "))
anos = 0
cont = 0
while(anos):
	if((ppentos+pbravos)<pportoreal):
		ppentos = ppentos + (ppentos*(tpentos//100))
		pbravos = pbravos + (pbravos*(tbravos//100))
		pportoreal = pportoreal + (pportoreal*(tportoreal//100))
	
	anos = anos + 1
print("Levará ", anos ," anos")