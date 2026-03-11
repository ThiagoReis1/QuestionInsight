from numpy import*
n = array(eval(input(" ")))
m = n[0]*2 + n[1]*2 + n[2]*6 + n[3]*1
p = 2,2,6,1
resultado = sum(m)/sum(p)
print(round(resultado, 2))