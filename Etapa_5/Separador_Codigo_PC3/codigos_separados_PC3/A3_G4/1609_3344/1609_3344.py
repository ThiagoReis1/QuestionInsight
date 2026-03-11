from numpy import*


a = array(eval(input("")))
b = input("").replace('R','L')	
			 
ac= -1
i = 0 

while(i<size(a)):
	if(a[i] == b):
		ac = i
	i= i +1			 
if(ac!=-1):
	print(ac)		 
else:
	print("NAO ENCONTRADA")