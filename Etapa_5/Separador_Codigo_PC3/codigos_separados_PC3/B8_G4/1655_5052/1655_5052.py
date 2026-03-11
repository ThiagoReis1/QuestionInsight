from numpy import*

s=input("Estados: ")
v=zeros(5, dtype=int)
w=s.split(',')

for i in range(size(w)):
	if w[i].upper()=="AC":
		v[0]=v[0]+1
	elif w[i].upper()=="AM":
		v[1]=v[1]+1
	elif w[i].upper()=="PA":
		v[2]=v[2]+1
	elif w[i].upper()=="RO":
		v[3]=v[3]+1
	elif w[i].upper()=="RR":
		v[4]=v[4]+1
print(max(v))
print(v)