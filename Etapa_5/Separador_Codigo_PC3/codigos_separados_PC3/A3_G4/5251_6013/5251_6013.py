c = input()
age = int(input())
c = c.lower()

i = 0

p = 0

if(age > 0) and (age<150):
	i = i +1
	if(c== "portovelho"):	
		p = 500
		i = i+1
	if(c=="santarem"):
		p= 370
		i=i+1
	if(c=="belem"):
		p= 600
		i= i+1
	if(c=="tefe"):
		p=360
		i=i+1
	if (c== "tabatinga"):
		p= 550
		i = i + 1
	if (age <= 2):
		p= 0
	if(age >= 3) and (age <= 12):
		p = p*0.5
	if (age>=65):
		p = p*0.7
		
if (i==2):
	print("Passagem: R$",round(p,2))
else:
	print("Entradas invalidas")


	