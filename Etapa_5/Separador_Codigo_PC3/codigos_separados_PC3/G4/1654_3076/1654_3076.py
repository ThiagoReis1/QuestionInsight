from numpy import*

v = input("").split(',')

vs = zeros(5, dtype=int)

am= 0
pe= 0
mg= 0
sp= 0
rs= 0


for i in range(size(v)):
	if(v[i] == "AM"):
		am = am + 1
	if(v[i] == "PE"):
		pe = pe + 1
	if(v[i] == "MG"):
		mg = mg + 1
	if(v[i] == "SP"):
		sp = sp + 1
	if(v[i] == "RS"):
		rs = rs + 1

vs[0] = am
vs[1] = pe
vs[2] = mg
vs[3] = sp
vs[4] = rs

print(max(vs))
print(vs)