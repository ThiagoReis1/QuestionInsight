from numpy import*
notas = array(eval(input("Notas: ")))
apr = 0
y = 0
k = 0
for i in notas:
	if(i>=5):
		apr = apr + 1
x = zeros(apr,dtype=int)
for z in notas:
	if(z>=5):
		z = k
		x[y] = z
		y = y + 1
		k = k + 1
	else:
		k = k + 1
print(apr)
print(x)