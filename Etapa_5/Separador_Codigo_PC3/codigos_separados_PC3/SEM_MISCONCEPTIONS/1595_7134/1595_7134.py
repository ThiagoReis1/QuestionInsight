from numpy import *
nts = array(eval(input("notas:")))
i = 0
total = 0

while i < size(nts):
	total = total + nts[i]
	i = i + 1

total = total - min(nts)
total = total/(size(nts)-1)
print(round(total,2))
		




