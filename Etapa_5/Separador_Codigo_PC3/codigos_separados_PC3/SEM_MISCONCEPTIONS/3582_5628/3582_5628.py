from numpy import *

arr = array(eval(input('Digite os valorres: ')))

total = sum(arr)

acum = 0

for i in range(size(arr)):
	if arr[i] > 160:
		acum = acum + 25
		
total2 = (total - acum)

print(round(total2,2))