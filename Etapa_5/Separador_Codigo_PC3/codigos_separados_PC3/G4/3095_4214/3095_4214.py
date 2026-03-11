c=input("Condicao:")

tot=0
lul=0
lel=0

v=3
e=2
d=1

while(c!="X"):
	if(c == "V"):
		
		tot= tot + v
		c=input("Condicao:")	
	elif(c == "E"):
		
		lul=lul+e
		c=input("condi:")
	elif(c == "D"):
		
		lel= lel + d
		c=input("Condi:")	
	else:
		c=input("segue:")

if(c=="X"):
	print(tot)
	print(lul)
	print(lel)
