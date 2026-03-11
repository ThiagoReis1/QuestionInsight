altura_chico = 1.5
taxa_chico = 0.02
anos= 0

altura= float (input ("digite a altura: "))
taxa= float (input ("digite a taxa: "))

while altura < altura_chico :
	altura_chico += taxa_chico
	altura += taxa
	anos += 1

print (anos)