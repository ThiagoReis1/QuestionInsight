from numpy import*
p = input("tom da pele: ").split(',')
cont = zeros(6, dtype = int)
i=0
a=0
b=0
c=0
d=0
e=0
f=0
while(i<size(p)):
	if(p[i]== 'MC'):
		a = a + 1
	elif(p[i] == 'C'):
		b= b + 1
	elif(p[i] == 'CM'):
		c = c+1
	elif(p[i]== 'EM'):
		d= d +1
	elif(p[i] == 'E'):
		e = e+1
	elif(p[i]== 'ME'):
		f= f+ 1
	i = i +1
cont[0]= a
cont[1]= b
cont[2]= c
cont[3]= d
cont[4]= e
cont[5]= f

print(max(cont))
print(cont)