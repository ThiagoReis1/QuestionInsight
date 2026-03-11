import numpy as np

tiros = np.array(eval(input()))
total = 10000

for i in tiros:
	if i == 1:
		total *=2
	elif i == 2:
		total = total
	elif i == 3:
		total /= 2
	else:
		total /= 4
		
print(round(total,2))