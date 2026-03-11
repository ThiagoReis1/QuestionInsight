string = input()
string = string.upper()
i=0
count=0
while(i<len(string)):
	if(string[i]=='A'):
		count+=0.15
	elif(string[i]=='E'):
		count+=0.15
	elif(string[i]=='I'):
		count+=0.15
	elif(string[i]=='O'):
		count+=0.15
	elif(string[i]=='U'):
		count+=0.15
	else:
		count+=0.17
	i+=1
print(round(count,2))