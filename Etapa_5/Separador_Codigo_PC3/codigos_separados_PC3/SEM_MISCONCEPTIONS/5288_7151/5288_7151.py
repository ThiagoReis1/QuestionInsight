idade=int(input("digite idade"))

total=0
cont_menores=0

while (idade!=-1):
	if (idade<18):
		cont_menores = cont_menores+1
	total=total+1
	idade=int(input("digite idade"))
	
print(total)
print(round(cont_menores/total*100,2))

	
	
	
