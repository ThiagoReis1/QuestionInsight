qo= int(input('qdade inicial'))
train= int(input('qdade grifos treinado semestre'))
count= int(input('qtade de grifos contaminados a cada semestre'))
t=0
qall = qo
while(qall>0):
	qall= qall+train-count
	t=t+1
print(t)
	