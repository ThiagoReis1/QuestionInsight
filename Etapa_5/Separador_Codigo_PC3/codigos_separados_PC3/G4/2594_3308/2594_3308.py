from numpy import*
d = array(eval(input("digite as demandas:")))
i = 1
x = 0
for i in range(1,size(d)) :
	if(d[1]>=d[0]):
		print(i)
		x = x + 1
print(x)
	