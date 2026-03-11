from numpy import*

c =input("Cor dos olhos: ").upper().split(',')
v0=[0,0,0,0,0]

for e in range(len(c)):
	if c[e]=='P':
		v0[0] = v0[0] + 1
	if c[e]=='C':
		v0[1] = v0[1] + 1
	if c[e]=='M':
		v0[2] = v0[2] + 1 
	if c[e]=='V':
		v0[3] = v0[3] + 1 
	if c[e]=='A':
		v0[4] = v0[4] + 1

print(max(v0))
print(array(v0))
