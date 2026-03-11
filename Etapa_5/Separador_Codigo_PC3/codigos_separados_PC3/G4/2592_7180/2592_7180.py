from numpy import *

meta = array(eval(input("Meta de vacinacao: ")))

count = 0
i = 0
j = 1

for i in meta[1:]:
	if i >= meta[0]:
		print(j)
		count = count+ 1
	j = j + 1
	

print(count)

