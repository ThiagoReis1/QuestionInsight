n=int(input("qte de alunos:"))
cont_l=0
cont_c=0
cont_p=0
c=0
while c<n:
	prato=input("prato:")
	c=c+1
	if prato.upper()=="L" or prato.upper()=="C" or prato.upper()=="P":
		if prato.upper()=="L":
			cont_l+=1
		if prato.upper()=="C":
			cont_c+=1
		if prato.upper()=="P":
			cont_p+=1
print("L= ",cont_l)
print("C= ",cont_c)
print("P= ",cont_p)