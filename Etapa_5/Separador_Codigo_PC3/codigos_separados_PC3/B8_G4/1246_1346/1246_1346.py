from numpy import*
vet = array(eval(input()))
A = min(vet)
B = max(vet)
C = 0.75*A + 0.25*B
D = 0.25*A + 0.75*B
v = zeros(2, dtype = "int")
for i in vet:
	if(i>=A and i<C):
		v[0]+=1
	elif(i>=C and i<D):
		v[1]+=1

print(v)		
