sim = int(input("Quantos clientes responderam sim")) 
nao = int(input()) 
 
while(sim != s): 
	
	if(nao < sim):
		nao = sim + s 
	sim = int(input())	

print("Quantos clientes responderam sim")