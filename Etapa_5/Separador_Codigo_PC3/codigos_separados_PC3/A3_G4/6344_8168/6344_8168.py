
v=input("")
i=0
a=0
while(i<len(v)):
	if(v[4]=="c" or v[4]=="C"):
		a=1
	else:
		a=2
	i+=1
if(a==1):
	print(v.upper())
else:
	print("nome invalido")