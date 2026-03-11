from numpy import*
s= input("pais:").split(',')
BE=0
ES=0
FR=0
IT=0
PT= 0
cont=zeros(5, dtype=int)
#quantidade do pais mais representativo
for i in range(0, len(s)):
	if(s[i]=="BE"):
		BE= BE +1
		cont[0]= BE
	elif(s[i]=="ES"):
		ES= ES+1
		cont[1]=ES
	elif(s[i]=="FR"):
		FR= FR +1
		cont[2]=FR
	elif(s[i]=="IT"):
		IT= IT +1
		cont[3]=IT
	elif(s[i]=="PT"):
		PT= PT+1
		cont[4]=PT

print(max(cont))

pessoas= zeros(5, dtype=int)
for i in range(0,len(s)):
	if(s[i]=="BE"):
		pessoas[0]= BE
	elif(s[i]=="ES"):
		pessoas[1]=ES
	elif(s[i]=="FR"):
		pessoas[2]=FR
	elif(s[i]=="IT"):
		pessoas[3]=IT
	elif(s[i]=="PT"):
		pessoas[4]=PT
	
print(pessoas)