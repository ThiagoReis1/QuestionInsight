# ysraele duany - 21650271

n = int(input("Insira a quantidade de termos:"))

x = 1
y = 1
t = 0
i = 1
while(n >= 1):
	if(i == 1):
		t = 1/7
	elif(i % 2 == 0):
		t = t + (x**0.5)/(6 + y)
	else:
		t = t - (x**0.5)/(6 + y)
	i = i + 1
	x = x + 1
	y = y + 2
print(round(t, 10))