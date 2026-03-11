from numpy import*
cor =  input("cor do cabelo: ")

cor = cor.split(',')

v = zeros(5,dtype=int)
s=0

for i in range(size(cor)):
	if(cor[i]=="P"):
		v[0]=v[0]+1
	elif(cor[i]=="C"):
		v[1]=v[1]+1
	elif(cor[i]=="R"):
		v[2]=v[2]+1
	elif(cor[i]=="L"):
		v[3]=v[3]+1
	elif(cor[i]=="B"):
		v[4]=v[4]+1

for i in range(size(v)):
	if(cor[i]==cor[i]):
		s=s+1
		
print(max(v))

print(v)