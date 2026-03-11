from numpy import * 
dd = array (eval(input('')))
i= 0 
pont = 0
while i < size (dd):
	if dd [i] == 1 or dd [i] == 3 or dd [i] == 5:
		pont += 10
	elif dd [i] == 2 or dd [i] == 4 or dd [i] == 6:
		pont += 5 
		
	i += 1 
print(round(pont, 2))