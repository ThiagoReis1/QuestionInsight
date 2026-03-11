from numpy import *

cl = array(eval(input()))
vetp = array([2,1,5])

nr = cl * vetp
medip = sum(nr)/sum(vetp)
print(round(medip,2))