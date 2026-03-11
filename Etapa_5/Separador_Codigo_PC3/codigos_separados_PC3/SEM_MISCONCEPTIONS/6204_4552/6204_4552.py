altura_macaco = 1.86
taxa_macaco = 0.01

hCoelho = float(input())
taxaCoelho = float(input())

anos = 0

while(hCoelho < altura_macaco):
	hCoelho += taxaCoelho
	altura_macaco += taxa_macaco
	
	anos+=1
	
print(anos)