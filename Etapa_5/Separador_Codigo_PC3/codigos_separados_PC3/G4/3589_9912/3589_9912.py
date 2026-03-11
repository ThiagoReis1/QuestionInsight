from numpy import*
v=array(eval(input("vetor: ")))
i=0
p=0

while i < size(v):
	if v[i] == 1:
		p=p+80
	if v[i] == 2:
		p=p+40
	if v[i] == 3:
		p=p+20
	if v[i] == 4:
		p=p+10
		
	i=i+1
print(p)