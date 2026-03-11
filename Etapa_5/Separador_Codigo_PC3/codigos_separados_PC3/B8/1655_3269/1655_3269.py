from numpy import*
o = input("").split(",")
res = zeros(5, dtype=int)

for i in range(size(o)):
	if(o[i] == "AC"):
		res[0]+=1
	elif(o[i] == "AM"):
		res[1]+=1
	elif(o[i] == "PA"):
		res[2]+=1
	elif(o[i] == "RO"):
		res[3]+=1
	elif(o[i] == "RR"):
		res[4]+=1
num_max = max(res)
print(num_max)
print(res)
		

