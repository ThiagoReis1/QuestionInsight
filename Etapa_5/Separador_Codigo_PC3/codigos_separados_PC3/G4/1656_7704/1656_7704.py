from numpy import*

pais= input().upper().split(',')

cont= zeros(5, dtype=int)

for i in range(len(pais)):
	if pais[i]== "BE":
		cont[0]+=1
	if pais[i]== "ES":
		cont[1]+=1
	if pais[i]== "FR":
		cont[2]+=1
	if pais[i]== "IT":
		cont[3]+=1
	if pais[i]== "PT":
		cont[4]+=1
print(max(cont))		
print(cont)

	
		
					
					