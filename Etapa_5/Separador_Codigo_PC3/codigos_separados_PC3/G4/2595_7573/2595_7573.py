from numpy import *

dem = array(eval(input("D: ")))

taxa = dem[0] 
i = 1
cont = 0 

for x in dem[1:]:
	if x <= taxa:
		cont = cont + 1
		print(i)
	i =i +1
print(cont)
	