from numpy import*
s = input("cor: ").upper().split(',')

vet = zeros(6,dtype = int)
for i in range(size(s)):
	if(s[i]=="MC"):
		vet[0] += 1
	elif(s[i]=="C"):
		vet[1] += 1
	elif(s[i]=="CM"):
		vet[2] += 1
	elif(s[i]=="EM"):
		vet[3] += 1
	elif(s[i]=="E"):
		vet[4] += 1
	elif(s[i]=="ME"):
		vet[5] += 1

print(max(vet))
print(vet)

