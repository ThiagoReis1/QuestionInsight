from numpy import*
v= input("").upper().split(',')
pr=0
ca=0
ru=0
lo=0
br=0

for i in range(len(v)):
	if(v[i]=="P"):
		pr=pr+1
	elif(v[i]=="C"):
		ca=ca+1
	elif(v[i]=="R"):
		ru=ru+1
	elif(v[i]=="L"):
		lo=lo+1
	elif(v[i]=="B"):
		br=br+1
		
		
