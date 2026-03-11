from numpy import*
cor = input("Digite as cores: ").split(",")
i = 0
vq = zeros(5,dtype=int)

for i in cor:
	if(i == "P"):
		vq[0] = vq[0]  + 1
	elif(i == "C"):
		vq[1] = vq[1]  + 1
	elif(i == "M"):
		vq[2] = vq[2]  + 1
	elif(i == "V"):
		vq[3] = vq[3]  + 1
	elif(i == "A"):
		vq[4] = vq[4]  + 1
		
print(max(vq))
print(vq)