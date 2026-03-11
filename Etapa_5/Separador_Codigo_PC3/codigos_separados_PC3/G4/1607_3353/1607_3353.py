from numpy import*

anda=array(eval((input("digite os andares: "))))
i=0
soma=0
tma=size(anda)
while(i<tma-1):
	soma=soma+((anda[i+1]-anda[i])*3)
	
	i=i+1

print(soma)