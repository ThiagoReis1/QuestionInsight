from numpy import*
vet = array(eval(input("tom: "))).upper()
vcont = zeros(6, dtype=int)
for i in range(0, size(vet)):
	if(vet[i]=="MC"):
		vcont[0]= vcont[0] + 1
	elif(vet[i]== "C"):
		vcont[1]= vcont[1]+ 1
	elif(vet[i] == "CM"):
		vcont[2]= vcont[2]+ 1
	elif(vet[i] == "EM"):
		vcont[3]= vcont[3]+1
	elif(vet[i] == "E"):
		vcont[4]== vcont[4]+1
	else:
		vcont[5]== vcont[5]+1
print(vcont)
		