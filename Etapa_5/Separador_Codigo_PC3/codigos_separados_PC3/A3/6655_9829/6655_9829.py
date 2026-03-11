from numpy import *

media = [5,1]

nota = array(eval(input("Insira nota: ")))
i = 0
maxi = size(nota)
calc = 0
calc = zeros(2, dtype=int)

while i < maxi:
	calc[i] = nota[i] * media[i]
	i+= 1

total = sum(calc)/6
print(round(total, 2))
	