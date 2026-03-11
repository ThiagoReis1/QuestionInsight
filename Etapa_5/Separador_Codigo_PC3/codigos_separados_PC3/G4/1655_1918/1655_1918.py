from numpy import*
v =  input("")
v = v.replace(",","")
c = zeros(5, dtype=int)
for i in range(0,len(v),2):
	if(v[i] + v[i+1] == "AC"):
		c[0] = c[0] + 1
	elif(v[i]+ v[i+1] == "AM"):
		c[1] = c[1] + 1
	elif(v[i]+ v[i+1] == "PA"):
		c[2] = c[2] + 1
	elif(v[i]+ v[i+1] == "RO"):
		c[3] = c[3] + 1
	else:
		c[4] = c[4] + 1
print(max(c))
print(c)
	