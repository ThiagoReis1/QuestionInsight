from numpy import*
n = input("insira: ").split(',')
d = zeros(5, dtype=int)

for i in range(size(n)):
	if(n[i]=="CHN"):
		d[0] = d[0] + 1
	elif(n[i]=="JPN"):
		d[1] = d[1] + 1
	elif(n[i]=="KOR"):
		d[2] = d[2] + 1
	elif(n[i]=="MGL"):
		d[3] = d[3] + 1
	elif(n[i]=="THA"):
		d[4] = d[4] + 1
		

print(max(d))
print(d)

