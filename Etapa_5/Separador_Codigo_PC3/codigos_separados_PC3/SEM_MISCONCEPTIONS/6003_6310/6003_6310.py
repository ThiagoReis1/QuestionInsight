numCenourasCompradas = int(input())
if(numCenourasCompradas < 5):
	total = numCenourasCompradas * 1.2
else:
	total = numCenourasCompradas * 0.9
print(round(total,2))