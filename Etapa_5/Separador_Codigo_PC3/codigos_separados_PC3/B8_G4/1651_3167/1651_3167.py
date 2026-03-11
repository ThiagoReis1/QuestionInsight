from numpy import*
vet = input().split(',')
x = zeros(6, dtype=int)
for i in vet:
	if(i == "MC"):
		x[0] = x[0]+ 1
	elif(i == "C"):
		x[1] = x[1]+1
	elif(i == "CM"):
		x[2] = x[2]+1
	elif(i == "EM"):
		x[3] = x[3]+1
	elif(i == "E"):
		x[4] = x[4]+1
	elif(i == "ME"):
		x[5] = x[4]+1
print(max(x))
print(x)




		
	