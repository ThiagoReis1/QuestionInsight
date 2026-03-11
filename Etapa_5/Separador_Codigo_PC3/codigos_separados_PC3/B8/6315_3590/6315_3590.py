entrada = input()
total = 0

j = 0;
i = 0
m = 0
s = 0
while(j < len(entrada)):
	if(entrada[j] == 'I'):
		i += 1
		total += 3.75
	elif(entrada[j] == 'M'):
		m += 1
		total += 4.50
	elif(entrada[j] == 'S'):
		s +=1
		total += 2.90
	j+= 1

print(round(total,2), end=' ')
print(i,end=' ')
print(m,end=' ')
print(s)
		