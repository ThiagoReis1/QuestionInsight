from numpy import*
x=input("udagyw:" ).split(',')
cont =zeros(5, dtype=int)

for i in x:
	if i.upper() == "AZ":
		cont[0]+=1
	elif i.upper() =="CA":
		cont[1]+=1
	elif i.upper() =="FL":
		cont[2]+=1
	elif i.upper() =="PA":
		cont[3]+=1
	elif i.upper() =="WI":
		cont[4]+=1
print(max(cont))
print(cont)