from numpy import*

tipo = array(eval(input("tipos: ")))

vcont = zeros(4, dtype = int)

for i in range(0, size(tipo)):
	if(tipo[i] == 1):
		vcont[0] = vcont[0] + 1
	elif(tipo[i] == 2):
		vcont[1] = vcont[1] + 1
	elif(tipo[i] == 3):
		vcont[2] = vcont[2] + 1
	elif(tipo[i] == 4):
		vcont[3] = vcont[3] + 1
		
print(vcont)
		

		
		
		

		
		
		