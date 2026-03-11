from numpy import * 

nome=input("Maior quantidade: ").split(',')
acumu=zeros(5,dtype=int)

for x in nome: 
	if x=="AZ":
		acumu[0]=acumu[0]+1
		
	elif x=="CA":
		acumu[1]=acumu[1]+1
		
	elif x=="FL":
		acumu[2]=acumu[2]+1
		
	elif x=="PA":
		acumu[3]=acumu[3]+1
		
	elif x=="WI":
		acumu[4]=acumu[4]+1
print(max(acumu))
print(acumu)

