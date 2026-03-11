idade=int(input())
menores=0
if(idade!=-1):
	while(idade != -1): 
		if(idade<18):
			menores=menores+1
				
		idade=int(input())
	print(menores)