from numpy import * 
 
m = array(input("Magia:").split(','))

n = array(eval(input("Nivel:")))

d = 0 

for i in range(size(m)):
	if(m[i] == "GELO"):
		d = d + (2 * n[i])
	elif(m[i] == "FOGO"):
		d = d + (3 * n[i])
	elif(m[i] == "CHOQUE"):
		d = d + (4 * n[i])
	elif(m[i] == "CONJURACAO"):
		d = d + (8 * n[i])
	elif(m[i] == "ILUSAO"):
		d = d + (10 * n[i])
		
print(d)