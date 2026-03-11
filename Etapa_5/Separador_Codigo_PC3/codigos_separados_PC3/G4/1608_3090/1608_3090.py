from numpy import*
v = array(eval(input("Numero total de pessoas no onibus: ")))
i = sum(v) - 75
j = i - v[-1]	
print(j)