from numpy import*


vet = array(eval(input("Primeiro vetor: ")))


while (size(vet) != 1):
    
	npar = 0

	for thing in vet:
		if (thing % 2 == 0):
			npar = npar + 1

 
	print(npar)

   
	print(size(vet)-npar)

		
	print(size(vet))


	vet = array(eval(input("Proximo vetor: ")))
