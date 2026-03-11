altura_macaco = 1.86
taxa_macaco = 0.01

am=float(input("altura do macaco: "))
fdp=float(input("altura do coelho: "))
			
anos = 0 

while am <= altura_macaco:
	altura_macaco += taxa_macaco
	am += fdp
	anos += 1
	
print(anos)