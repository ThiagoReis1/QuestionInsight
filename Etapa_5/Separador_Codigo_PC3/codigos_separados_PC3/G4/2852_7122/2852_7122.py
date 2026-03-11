from  numpy import*

c = array(eval(input(": ")))

i = 0

for x in c:
	if x == 88:
		i = i / 2
	else:
		i = i + x
		
print(i)
		