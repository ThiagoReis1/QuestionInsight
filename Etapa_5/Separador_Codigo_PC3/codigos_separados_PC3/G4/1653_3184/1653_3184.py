from numpy import*
st = input("").upper().split(',')
result = zeros(5, dtype=int)
i = 0
ar = 0
br = 0
cl = 0
co = 0
uy = 0

while(size(st)>i):
	if(st[i]=="AR"):
		ar = ar + 1
	if(st[i]=="BR"):
		br = br + 1
	if(st[i]=="CL"):
		cl = cl + 1
	if(st[i]=="CO"):
		co = co + 1
	if(st[i]=="UY"):
		uy = uy + 1
	i = i + 1

result[0]=ar
result[1]=br
result[2]=cl
result[3]=co
result[4]=uy

print(max(result))
print(result)