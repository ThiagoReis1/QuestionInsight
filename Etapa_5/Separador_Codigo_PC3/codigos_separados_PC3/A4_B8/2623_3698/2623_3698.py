from numpy import*
t = array(eval(input(':')))
col = shape(t)[1]
x=0
total = zeros(col, dtype=float)
for j in range(col):
	x=x+t[:,j]
	total[0]=min(x)
print(total)

if (total[0]>total[1]) and (total[0]>total[2]) and (total[0]>total[3]):
	print="1"
elif (total[1]>total[0]) and (total[1]>total[2]) and (total[1]>total[3]):
	print="2"
elif (total[2]>total[1]) and (total[2]>total[0]) and (total[2]>total[3]):
	print="3"
