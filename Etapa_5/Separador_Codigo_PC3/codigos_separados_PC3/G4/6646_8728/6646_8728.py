from numpy import*
v = array([1,2,3])

n = array(eval(input("notas:")))

s = v * n 

x = sum(s)/6
print(round(x,2))