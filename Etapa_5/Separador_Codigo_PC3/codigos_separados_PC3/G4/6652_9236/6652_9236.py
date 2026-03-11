from numpy import*
vn = array(eval(input(" ")))
m = vn[0]*2 + vn[1]*2 + vn[2]*6 + vn[3]*1
peso = 2,2,6,1
mp = m / sum(peso)

print(round(mp, 2))