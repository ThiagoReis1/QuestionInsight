from numpy import*
v = array(eval(input("")))

aux = [9,8,7,6,5,4,3,2,1]

ts = (v[0]*1) + (v[1]*2) + (v[2]*3) + (v[3]*4) + (v[4]*5) + (v[5]*6) + (v[6]*7) + (v[7]*8) + (v[8]*9)

s = ts%11

print(s)