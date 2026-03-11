from numpy import * 

v=array(eval(input("insira:")))
c=len(v)
d=0

for freq in v:
	if freq >= 70:
		c+=1
		
v_passaram = zeros(c,dtype=int)
d=0

for i in range(c):
	if v[i] >= c :
		v_passaram[d] = i 
		d+=1

print(c)
print(v_passaram)
