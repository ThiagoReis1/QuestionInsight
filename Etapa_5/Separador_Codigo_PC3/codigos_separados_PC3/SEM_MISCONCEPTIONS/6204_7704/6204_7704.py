altura_macaco = 1.86
taxa_macaco = 0.01

altura_coelho= float(input())
taxa_coelho= float(input())

cont=0

while altura_macaco>=altura_coelho:
	altura_coelho=altura_coelho+taxa_coelho
	altura_macaco=altura_macaco+taxa_macaco
	cont= cont+1
	
print(cont)
	
	
	
	
	
	
	
	