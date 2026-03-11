v = int(input("População inicial de tracajás no viveiro:"))
x = int(input("Taxa anual de crescimento do número de tracajás (em %):"))
y = int(input("Número de tracajás roubados anualmente:"))

t = 1
m = v
k = 500
h = y
while(m > y):
	t = t + 1
	m = (m + (m * x/100)) - y -k
print(t)	