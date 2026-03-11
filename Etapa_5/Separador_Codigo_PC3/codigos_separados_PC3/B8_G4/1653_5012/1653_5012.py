from numpy import*

v = input("nacionalidade:").split(",")

s = zeros(5,dtype=int)

for i in range(size(v)):
	if(v[i].lower() == "ar"):
		s[0]= s[0] + 1
	elif(v[i].lower() == "br"):
		s[1]= s[1] + 1
	elif(v[i].lower() == "cl"):
		s[2] = s[2] + 1
	elif(v[i].lower() == "co"):
		s[3] =s[3] + 1
	elif(v[i].lower() == "uy"):
		s[4] = s[4] + 1
print(max(s))
print(array(s))