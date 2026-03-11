from numpy import*

n = array(eval(input()))
b = array(eval(input().upper()))

j = 0
df = 0
while (j < size(n)):
	if (b[j] == "QUENTE"):
		df = df + n[j]*90
	elif (b[j] == "MORNO"):
		df = df + n[j]*45
	elif (b[j] == "FRIO"):
		df = df + n[j]*0
	j = j + 1
df = df * 0.005
print(round(df,2))