from numpy import*

v = array(eval(input("Vetor: ")))

p = float(200)
i = 0

while(i<size(v)):
    if(v[i] == 1):
        p = 4*p
    elif(v[i] == 2):
        p = 2*p
    elif(v[i] == 3):
        p = p
    elif(v[i] == 4):
        p = p/2
    i += 1
print(p)