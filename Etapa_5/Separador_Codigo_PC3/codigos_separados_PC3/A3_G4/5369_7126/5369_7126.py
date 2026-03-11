from numpy import*
x= array(eval(input("digite o vetor")))

aux=[9,8,7,6,5,4,3,2,1]

s=(x[0]*9)+(x[1]*8)+(x[2]*7)+(x[3]*6)+(x[4]*5)+(x[5]*4)+(x[6]*3)+(x[7]*2)+(x[8]*1)

ts= s%11

print(ts)
