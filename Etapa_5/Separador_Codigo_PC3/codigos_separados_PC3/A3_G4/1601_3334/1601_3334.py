from numpy import*

v = array(eval(input("Vetor: ")))
i = 0
g = 0
while (i < size(v)):
    if(v[i]==min(v)):
        g=i
    i += 1
print(g)

