n = int(input())
c = 0 
i = 0 

while(n != 0):
	if(n > 0):
		i = i + 1
		if(n%3 == 0):
			c = c + 1
	n = int(input())

print(i)
print(round((c/i)*100, 2))