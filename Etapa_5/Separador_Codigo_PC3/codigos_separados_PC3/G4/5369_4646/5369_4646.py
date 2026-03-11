from numpy import*
v =array(eval(input("cpf")))
vn  = [9,8,7,6,5,4,3,2,1]
i= 0
d = 0
while(i<size(v)):
	d = d + v[i]*vn[i]
	i=i+1
r = d%11
print(r)
