from numpy import*

vetor = array(eval(input("temperaturas: ")))

t = 0
i = 0

while(i<size(vetor)):
	if(vetor[i]>0 and vetor[i]<40):
		t = t + 1
	i = i +1
	
tem = array(zeros,t, dtype = float)
i = 0
k = 0

while(i<size(tem)):
	if(tem[i]>0 and tem[1]<40):
		tem = temp[i]
		k = k + 1
	i = i + 1
	print(tem)
		