br = int(input())
pt = int(input())
pr = int(input())
tb = float(input())
tp = float(input())
tpr = float(input())

anos = 1
soma = br + pt
while(soma < pr):
 br = br + (br*(tb/100))
 pt = pt + (pt*(tp/100))
 pr = pr + (pr*(tpr/100))
 soma = br + pt	
 anos += 1	
print(anos)