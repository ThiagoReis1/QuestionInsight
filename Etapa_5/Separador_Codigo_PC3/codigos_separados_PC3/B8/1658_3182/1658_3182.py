from numpy import*
v=input("digite o vetor").upper().split(',')
x=zeros(5, dtype=int)
cont=0
cont1=0
cont2=0
cont3=0
cont4=0
for i in range(size(v)):
	if(v[i]=="CHN"):
		cont=cont+1
	elif(v[i]=="JPN"):
		cont1=cont1+1
	elif(v[i]=="KOR"):
		cont2=cont2+1
	elif(v[i]=="MGL"):
		cont3=cont3+1
	elif(v[i]=="THA"):
		cont4=cont4+1
x[0]=cont
x[1]=cont1
x[2]=cont2
x[3]=cont3
x[4]=cont4
print(max(x))
print(x)
		
	
