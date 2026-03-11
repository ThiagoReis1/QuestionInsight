from numpy import*
nacionalidades = input("Digite o vetor:").split(',')
resultado = zeros(5, dtype = int)

for i in range(len(nacionalidades)):
	if nacionalidades[i] == "AR":
		resultado[0] += 1
		
	elif nacionalidades[i] == "BR":
		resultado[1] += 1
		
	elif nacionalidades[i] == "CL":
		resultado[2] += 1
		
	elif nacionalidades[i] == "CO":
		resultado[3] += 1
		
	elif nacionalidades[i] == "UY":
		resultado[4] += 1

print(max(resultado))
	
print(resultado)
	
