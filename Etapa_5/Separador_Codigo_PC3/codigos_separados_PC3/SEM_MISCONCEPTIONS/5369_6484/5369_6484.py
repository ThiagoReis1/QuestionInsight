from numpy import*

v = array(eval(input()))
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]

total = v[0]*y[0] + v[1]*y[1] + v[2]*y[2] + v[3]*y[3] +v[4]*y[4] + v[5]*y[5] + v[6]*y[6] + v[7]*y[7] + v[8]*y[8]
print(total%11)