# faça seu código aqui!
nm = int(input("numero de alunos:" ))
l = 0
c = 0
p = 0
n = 0

while n < nm:
	o = input("opcao: ").upper()
	n = n + 1
	
	if o =="L": l+=1
	elif o =="C": c+=1
	elif o =="P": p+=1
		
print("L=", l)
print("C=", c)
print("P=", p)
	