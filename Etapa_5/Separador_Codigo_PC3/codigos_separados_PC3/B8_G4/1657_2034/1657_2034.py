from numpy import*
vet= array(eval(input("Digite os estados:")))
az=0
ca=0
fl=0
pa=0
wi=0
for i in range(size(vet)):
	if(vet[i]=="AZ"):
		az=az+1
	elif(vet[i]=="CA"):
		ca=ca+1
	elif(vet[i]=="FL"):
		fl=fl+1
	elif(vet[i]=="PA"):
		pa=pa+1
	elif(vet[i]=="WI"):
		wi=wi+1
vet2=array([az,ca,fl,pa,wi])
print(max(vet2))
print(vet2)

#ESSA DISCIPLINA É UMA MEEERRRDAAAA


		
	

		