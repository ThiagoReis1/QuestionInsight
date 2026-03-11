from numpy import*
num = array(eval(input("insira as notas: ")))
x = array([4,3])
t = len(num) - 1
i = 0
s = 0

while i <= t:
	s = s + num[i]*x[i]
	i += 1
m = s/sum(x)
print(round(m,2))