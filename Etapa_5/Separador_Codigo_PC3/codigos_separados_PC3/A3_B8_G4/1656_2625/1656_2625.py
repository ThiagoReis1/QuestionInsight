from numpy import*

string = input(" ")
string1 = string.split(',')
i = 0
a = 0
b = 0
c = 0
d = 0
e = 0
z = 0
v = zeros(5, dtype = int)

while(i<len(string1)):	
	if(string1[i] == "BE"):
		a = a + 1
		
	elif(string1[i] == "ES"):
		b = b + 1
		
	elif(string1[i] == "FR"):
		c = c + 1
		
	elif(string1[i] == "IT"):
		d = d + 1
	
	elif(string1[i] == "PT"):
		e = e + 1
	i = i + 1
v[0] = a
v[1] = b
v[2] = c
v[3] = d
v[4] = e
print(max(v))
print(v)
