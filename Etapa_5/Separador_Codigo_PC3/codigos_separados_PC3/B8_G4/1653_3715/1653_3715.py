from numpy import*
cont = zeros(5, dtype=int)
vet = input("").upper().split(',')
for x in vet:
	if (x=='AR'):
		cont[0] = cont[0]+1
	elif (x=='BR'):
		cont[1] = cont[1]+1
	elif (x=='CL'):
		cont[2] = cont[2]+1
	elif (x=='CO'):
		cont[3] = cont[3]+1
	elif (x=='UY'):
		cont[4] = cont[4]+1
		
x = sorted(cont)
print(x[4])		
print(cont)