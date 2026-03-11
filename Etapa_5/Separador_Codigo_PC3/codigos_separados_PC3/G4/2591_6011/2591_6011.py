from numpy import*

a = array(eval(input("")))
p = abs(a[0])
cont =0

for i in range(1,size(a)):
	if((a[i]<0)and (abs(a[i])>=p)):
		print(i)
		cont = cont+1
print(cont)

		
		