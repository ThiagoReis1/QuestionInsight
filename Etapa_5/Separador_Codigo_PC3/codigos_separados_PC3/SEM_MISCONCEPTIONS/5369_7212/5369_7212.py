from numpy import*

c= array(eval(input()))

v= [9,8,7,6,5,4,3,2,1]

cont1=0
cont2=0

while(cont1 < size(c)):
		
		cont2= cont2 + (c[cont1] * v[cont1])
		
		cont1 = cont1 + 1

s=cont2 % 11


print(s)
		
		