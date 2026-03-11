from numpy import*

x = array(eval(input("Notas do aluno: ")))
n = size(x) - 1

y = zeros ( n , dtype = float)

i = 0
j = 0

while ( i < size(x)):
	if (x[i] != min(x)):
		y[j] = x[i]
		j = j + 1
	i = i + 1
	
Mf = sum(y) / size(y)
print(round(Mf , 2))

if (Mf >= 5.0):
	print("APROVOU")
else:
	print("REPROVOU")