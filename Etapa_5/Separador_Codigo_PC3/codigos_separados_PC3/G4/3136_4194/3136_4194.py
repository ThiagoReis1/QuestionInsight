from numpy import*
x = array(eval(input("Num positivos: ")))
y = 0

for i in range(size(x)):
	y = y + log(x[i] + 1)
	w = size(x)
	z = exp(sum(y)/w)-1

print(round(z, 2))
