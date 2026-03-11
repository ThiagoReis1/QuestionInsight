anos = 1
x = float(input("Numero inicial T: "))
y = float(input("Numero inicial P:"))
taxaT = float(input("Taxa de crescimento tambaquis: "))
taxaP = float(input("Taxa de crescimento pacus: "))
NM = (float(input("Numero maximo de especies comportadas: ")))
while (x+y <= NM):
	x = (x + x*taxaT)
	y = (y + y*taxaP)
	anos = anos + 1
print (anos)