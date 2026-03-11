from numpy import*

vetor=input(":").split(",")

final=zeros(5,dtype(int))

for i in vetor:
	if i=="CHN":
		final[0]=final[0]+1
	if i=="JPN":
		final[1]=final[1]+1
	if i=="KOR":
		final[2]=final[2]+1
	if i=="MGL":
		final[3]=final[3]+1
	if i=="THA":
		final[4]=final[4]+1
print(max(final))
print(final)

