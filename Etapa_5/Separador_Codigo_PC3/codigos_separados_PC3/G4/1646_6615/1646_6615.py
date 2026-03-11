from numpy import*
sqs=array(eval(input("saques: ")))
j = 0
mini = 0
for i in range(size(sqs)):
	if(sqs[i]<=50):
		mini = mini + 1
ind = zeros(mini, dtype=int)
for i in range(size(sqs)):
	if(sqs[i]<=50):
		ind[j]=i
		i = i + 1
		j = j + 1
print(mini)
print(ind)
	