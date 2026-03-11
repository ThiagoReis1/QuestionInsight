from numpy import*

vt = array(eval(input()))
vt2 = array([3, 2, 4, 1, 3])

media = (vt[0]*vt2[0] + vt[1]*vt2[1] + vt[2]*vt2[2] + vt[3]*vt2[3] + vt[4]*vt2[4]) / (vt2[0]+vt2[1]+vt2[2]+vt2[3]+vt2[4])

print(round(media, 2))