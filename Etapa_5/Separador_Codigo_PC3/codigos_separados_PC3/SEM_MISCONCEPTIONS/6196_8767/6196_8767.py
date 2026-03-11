altura_chico = 1.5
taxa_chico = 0.02
cont = 0 

alt = float(input())
tx = float(input())

while alt < altura_chico:
	cont = cont + 1 
	alt = alt + tx
		
	altura_chico = altura_chico + taxa_chico

print(cont)
#print(alt)
	