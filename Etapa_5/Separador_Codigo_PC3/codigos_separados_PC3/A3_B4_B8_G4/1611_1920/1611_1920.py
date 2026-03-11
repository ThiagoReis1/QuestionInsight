from numpy import*
v = array(input())
cv = 0
cc = 0
i = 0
while (i<size(v)):
	if ("A"== v[i]):
		cv +=1
	elif ("E"== v[i]):
		cv +=1
	elif ("I"== v[i]):
		cv +=1
	elif ("O"== v[i]):
		cv +=1
	elif ("U"== v[i]):
		cv +=1
	i += 1
	print(i)
	print(size(v))
print (cv)
	
	