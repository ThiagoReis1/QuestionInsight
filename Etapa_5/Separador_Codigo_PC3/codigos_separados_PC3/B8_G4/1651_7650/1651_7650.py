from numpy import*

tp = input("vetor:").split(',')
vac = zeros(6 , dtype = int)

for i in range (size(tp)):
	if(tp[i] == "MC"):
		vac[0] += 1
	elif(tp[i] == "C"):
		vac[1] += 1
	elif(tp[i] == "CM"):
		vac[2] += 1
	elif(tp[i] == "EM"):
		vac[3] += 1 
	elif(tp[i] == "E"):
		vac[4] += 1
	elif(tp[i] == "ME"):
		vac[5] += 1
		
print(max(vac))
print(vac)