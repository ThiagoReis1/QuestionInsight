from numpy import*
v = input(": ").split(',')
vetor = zeros(5, dtype = int)
chn = 0
jpn = 0
kor = 0
mgl = 0
tha = 0
for i in v:
	if(i.lower() == "chn"):
		chn = chn + 1
	elif(i.lower() == "jpn"):
		jpn = jpn + 1
	elif(i.lower() == "kor"):
		kor = kor + 1
	elif(i.lower() == "mgl"):
		mgl = mgl + 1
	elif(i.lower() == "tha"):
		tha = tha + 1
vetor[0] = vetor[0] + chn
vetor[1] = vetor[1] + jpn
vetor[2] = vetor[2] + kor
vetor[3] = vetor[3] + mgl
vetor[4] = vetor[4] + tha
print(max(vetor))
print(vetor)

	