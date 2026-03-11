from numpy import *

vn = array(eval(input()), dtype = int)
va = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total_soma = vn[0]*va[0] + vn[1]*va[1] + vn[2]*va[2] + vn[3]*va[3] + vn[4]*va[4] + vn[5]*va[5] + vn[6]*va[6] + vn[7]*va[7] + vn[8]*va[8]

resto = total_soma % 11

print(resto)