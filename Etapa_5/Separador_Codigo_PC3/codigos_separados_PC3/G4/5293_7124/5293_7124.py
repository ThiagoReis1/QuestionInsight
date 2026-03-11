x= int(input())
cont= 0
cont1=0
while (x!=0):
	cont= cont+1
	if (x%2==0):
		cont1=cont1+1
	x= int (input())
	
s= cont1*100/cont
print (cont)
print (round(s,2))