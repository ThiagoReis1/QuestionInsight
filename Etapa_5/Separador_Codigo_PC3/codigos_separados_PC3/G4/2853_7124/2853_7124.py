from numpy import*
s= array(eval(input("notas:")))
c= 0

for i in range(size(s)):
	if s[i]== 10:
		c= c*10
	else:
		c= c+ s[i]
print(c)
	
	
	