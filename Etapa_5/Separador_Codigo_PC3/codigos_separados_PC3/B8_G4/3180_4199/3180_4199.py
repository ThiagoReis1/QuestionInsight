from numpy import*
vets = array(eval(input("tipo de soro")))
vetf = zeros(4,dtype=int)
for i in range(size(vets)):
	if( vets[i] == 1):
		vetf[0] = vetf[0] + 1
	elif(vets[i] == 2):
		vetf[1] = vetf[1] + 1
	elif(vets[i]==3):
		vetf[2] = vetf[2] + 1
	elif(vets[i]== 4):
		vetf[3] = vetf[3] + 1
		
print(vetf)