from numpy import*
et=input("Etinias: ").split(',')
v=zeros(5,dtype=int)

for i in range(size(et)):
	if et[i]=="B":
		v[0]+=1
	elif et[i]=="PA":
		v[1]+=1
	elif et[i]=="PR":
		v[2]+=1
	elif et[i]=="A":
		v[3]+=1
	elif et[i]=="I":
		v[4]+=1
print(max(v))
print(v)
		