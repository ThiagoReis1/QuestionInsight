from numpy import*
n = array(eval(input("Digite as notas: ")))

m = ((n[0]*3)+ (n[1]*2)+ (n[2]*4)+ (n[3]*1) + (n[4]*3))/13
print(round(m,2))