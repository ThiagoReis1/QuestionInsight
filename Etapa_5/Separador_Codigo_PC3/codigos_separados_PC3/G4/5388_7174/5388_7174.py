from numpy import * 
pa=input("txt:")
i=0
p=0
while(i!=len(pa)):
	if(pa[i]=="A" or pa[i]=="E" or pa[i]=="U" or pa[i]=="O" or pa[i]=="I"):
		p=p+25.12
		i=i+1
	else:
		p=p+40.18
		i=i+1
print(round(p,2))
		