na = float(input("Numero de habitantes da cidade Bravos:"))
nb = float(input("Numero de habitantes da cidade Pentos:"))
nc = float(input("Numero de habitantes da cidade Porto Real:"))
pa = float(input("Digite o cp da cidade Bravos:"))
pb = float(input("Digite o cp da cidade Pentos:"))
pc = float(input("Digite o cp da cidade Porto Real:"))
numa = na
numb = nb
numc = nc
pera = pa*0.01
perb = pb*0.01
perc = pc*0.01
a = 1

while((numa + numb) < numc):
	numa = numa + (numa*pera)
	numb = numb + (numb*perb)
	numc = numc + (numc*perc)
	a = a + 1
print(a)