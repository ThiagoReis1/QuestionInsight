from numpy import *

v = array(eval(input("v: ")))

m = sum(v)-min(v)
n = size(v)-1
print(m/n)