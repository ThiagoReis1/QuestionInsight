from numpy import*
p = float(input("informe o numero real: "))
x = array(eval(input("primeiro vetor: ")))
y = array(eval(input("seundo vetor: ")))
t = p/(p + 1)
n = 0

for i in range(size(x)):
	n = n + ((abs(x[i] - y[i])) ** t)
j = n ** (1/t)
print(round(j,4))