from numpy import*
u = array(eval(input('')))
s=0
for i in u:
	if i >40:
		s=s-2.5+i
else:
   s=s+i
print(round(sum(u)- 2.5,2))
