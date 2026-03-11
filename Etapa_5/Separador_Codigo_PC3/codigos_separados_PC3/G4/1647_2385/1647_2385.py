from numpy import*
vet=array(eval(input()))
x=0
y=0

for i in vet:
	if(i>=70):
		x=x+1
	y=y+1
	
nv = zeros(x, int)
f=0
y=0
for i in vet:
	if(i>=70):
		nv[f]= y
		f=f+1
	y=y+1

print(x)
print(nv)