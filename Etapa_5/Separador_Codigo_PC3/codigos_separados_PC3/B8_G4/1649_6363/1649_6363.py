from numpy import*

v = input("").upper().split(',')
a = ("P,C,M,V,A").split(',')
vc = zeros(size(v), dtype=int)
w = zeros(size(a), dtype=int)

for i in range(size(v)):
	if(v[i].upper()=="P"):
		vc[0] = vc[0] + 1
		w[0] = vc[0]
	elif(v[i].upper()=="C"):
		vc[1] = vc[1] + 1
		w[1] = vc[1]
	elif(v[i].upper()=="M"):
		vc[2] = vc[2] + 1
		w[2] = vc[2]
	elif(v[i].upper()=="V"):
		vc[3] = vc[3] + 1
		w[3]= vc[3]
	elif(v[i].upper()=="A"):
		vc[4] = vc[4] + 1
		w[4] = vc[4]

print(max(vc))
print(w)