from numpy import*

v = array(eval(input("")))
n = int(input(""))
cont = 0
i = 0
while(i<size(v)):
	if (v[i]>n):
		cont = cont+1
	elif (v[i]==n):
		print(i)
	i = i+1
print(cont)
      

		

	
	