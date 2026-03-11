fr = 4.0 
sg = 3.14
od = 10.0
a = float(input("quantidade de fr: "))
b = float(input("quantidade de sg: "))
c = float(input("quantidade de od: "))
raz1 = int(a/fr)
raz2 = int(b/sg)			 
raz3 = int(c/od)
quantidade = min(raz1,raz2,raz3)
print(round(quantidade,0))