from numpy import*
vnum = array(eval(input("Vetor de numeros: ")))

i = 0
pont = 0

while(i < size(vnum)):
	if(vnum[i] == 1):
		pont = pont + 80
		
	if(vnum[i] == 2):
		pont = pont + 40
		
	if(vnum[i] == 3):
		pont = pont + 20
	
	if(vnum[i] == 4):
		pont = pont + 10
		
	i = i + 1
	
print(pont)
