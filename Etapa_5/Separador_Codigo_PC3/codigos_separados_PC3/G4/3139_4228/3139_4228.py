from numpy import*
v = array(eval(input("Numero Real: ")))
v = v**(1/3)

m = ((sum(v)/size(v))**3)
print(round(m, 2))