from numpy import*

s=input("Digite uma string qualquer: ")

v=0
v1=0
v2=0
v3=0
v4=0
c=0

for i in range(len(s)):
	if(s[i].upper()=="A"):
		v=v+1
	elif(s[i].upper()=="E"):
		v1=v1+1
	elif(s[i].upper()=="I"):
		v2=v2+1
	elif(s[i].upper()=="O"):
		v3=v3+1
	elif(s[i].upper()=="U"):
		v4=v4+1
	elif(s[i].upper()!="A" and s[i].upper()!="E" and s[i].upper()!="I" and s[i].upper()!="O" and s[i].upper()!="U"):
		c=c+1

print(v+v1+v2+v3+v4)
print(c)
		
		