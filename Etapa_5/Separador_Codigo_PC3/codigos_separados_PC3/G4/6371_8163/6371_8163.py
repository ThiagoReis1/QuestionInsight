from numpy import*

num= array(eval(input("digite os numeros: ")))

i=0
for i in range(size(num)):
	if num[i] == 0:
		n= 9
	else :
		n= num[i]-1
	num[i]=n**2	
print(num)
		