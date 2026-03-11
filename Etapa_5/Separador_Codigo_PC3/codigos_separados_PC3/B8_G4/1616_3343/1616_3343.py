from numpy import*

m = array(eval(input("vetor tipo de magia:")))
n = array(eval(input("nivel do mago:")))
i = 0
d = 0

while(i < size(n)):
	if(m[i] == "GELO" ):
		d = d + 2*n[i]	
	elif(m[i] == "FOGO"):
		d = d + 3*n[i]
	elif(m[i] == "CHOQUE"):
		d = d + 4*n[i]
	elif(m[i] == "CONJURACAO"):
		d = d + 8*n[i]
	elif(m[i] == "ILUSAO"):
		d = d + 10*n[i]
		
	i = i + 1
	
print(d)	