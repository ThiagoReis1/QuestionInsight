from numpy import*

s=input("digite ").upper().split(',')

v=zeros(4,dtype=int)

for i in range(len(s)):
	if(s[i]=='A'):
		v[0]=v[0]+1
	
	elif( s[i]== 'P'):
		v[1]=v[1]+1
	
	elif(s[i]== 'D'):
		v[2]=v[2]+1
		
	elif(s[i]=='M'):
		v[3]=v[3]+1
print(v)