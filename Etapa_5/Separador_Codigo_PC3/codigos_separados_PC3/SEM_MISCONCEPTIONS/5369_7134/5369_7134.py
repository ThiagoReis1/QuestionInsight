from numpy import *
num = array(eval(input("nove primeiros dgts:")))
totalS = (num[0]*9)+(num[1]*8)+(num[2]*7)+(num[3]*6)+(num[4]*5)+(num[5]*4)+(num[6]*3)+(num[7]*2)+(num[8])
total = totalS%11
print(total)

