from numpy import *
p = array(eval(input("P: ")))
q = array(eval(input("Q: ")))

d = ((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[-1] - q[-1])**2)**0.5
print(round(d, 4)
sim = 1/(1 + d)
print(round(sim, 2))

