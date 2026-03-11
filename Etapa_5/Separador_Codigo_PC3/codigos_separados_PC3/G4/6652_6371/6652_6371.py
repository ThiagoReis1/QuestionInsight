from numpy import*

n = array(eval(input()))
p = [2,2,6,1]
np = n[0]*p[0]+n[1]*p[1]+n[2]*p[2]+n[3]*p[3]
media =np/11
print(round(media,2))