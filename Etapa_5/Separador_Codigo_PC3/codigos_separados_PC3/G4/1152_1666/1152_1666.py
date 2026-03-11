haba = int(input("Numero de habitantes de Bravos: "))
habb = int(input("Numero de habitantes de Pentos: "))
habc = int(input("Numero de habitantes de porto real: "))
tbravos = float(input("Taxa de crescimento de Bravos: "))
tpentos = float(input("Taxa de crescimento de Pentos: "))
tporto_real = float(input("Taxa de crescimento de Porto Real: "))

popa = haba
popb = habb
popc = habc
anos = 1
ta = tbravos * 0.01
tb = tpentos * 0.01
tc = tporto_real * 0.01

while ( popa + popb < popc ):
	popa = popa  + (popa* ta)
	popb = popb  + (popb* tb)
	popc = popc  + (popc* tc)
	anos = anos + 1
print(anos)
