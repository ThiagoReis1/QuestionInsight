cont = 0
contr = 0
al = input("aluno?")
x = al.upper()
while(contr < 1):
	if(x == "ICOMP"):
		cont = cont+1
		al = input("aluno?")
		x = al.upper()
	elif(x == "S"):
		contr = 1
	else:
		al = input("aluno?")
		x = al.upper()
print(cont)
