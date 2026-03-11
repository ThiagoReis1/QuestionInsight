x = int(input())
total = 0
if x < 5:
	total += x*1.2
else:
	total+=x*0.9
print(round(total,2))