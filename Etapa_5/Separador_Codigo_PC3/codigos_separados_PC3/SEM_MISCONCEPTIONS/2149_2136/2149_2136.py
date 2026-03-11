from numpy import*
n1= array(eval(input("notas: ")))
n2 = array(eval(input("notas: ")))
x = zeros(size(n1))
i=0
ap=0
z =0 
while(i<size(n1)):
	for x in n1:
		if((n1[i]+ n2[i])>=12):
			ap = ap +1
	i = i +1
x[0]=n1[0]+n2[0]
x[1]=n1[0]+n2[0]
x[2]=n1[2]+n2[2]

	print(x)
	print(ap)
			







