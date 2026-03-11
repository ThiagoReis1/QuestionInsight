from numpy import *

saque = array(eval(input('')))
con = 0

for i in range(size(saque)):
	if saque[i] <= 50 :
		con +=1
ind = zeros(con, dtype='int')
print(con)
j=0

for i in range(size(saque)):
	if saque[i] <= 50:
		ind[j] = i
		j +=1
print(ind)