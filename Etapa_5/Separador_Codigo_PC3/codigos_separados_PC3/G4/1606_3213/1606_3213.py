from numpy import *

an = array(eval(input("Andar: ")))

i = 0
a = 2
ac = 0

while (i < size(an) and a > i):
	b = an[i] - an[i:a]
	ac = ac + abs(b)
	a = a + 1
	i = i + 1
print(ac[1])