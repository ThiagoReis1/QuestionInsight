from numpy import *
finalnotes = array(eval(input("insert value of notes: ")))
score = 0
for i in range(size(finalnotes)):
	if(finalnotes[i]<5):
		score = score + 1
reproved = zeros(score,dtype=int)
fscore = 0
for g in range(size(finalnotes)):
	if(finalnotes[g]<5):
		reproved[fscore] = g
		fscore = fscore + 1
print(score)
print(reproved)