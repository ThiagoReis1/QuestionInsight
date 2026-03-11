from numpy import* 
v = array(eval(input()))
i = 0
f = []
while(i < size(v)):
    if(v[i] > 80):
        es = v[i] * (0.15)
        desconto = v[i] - es
    elif(v[i] < 80):
        desconto = v[i]
    i = i + 1
    f = f + [desconto]
    t = sum(f)
print(round(t,2))
