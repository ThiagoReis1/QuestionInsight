ramem=float(input("quantidade de ramem:"))
menma=float(input("quantidade de menma:"))
bolinho= float(input("quantidade de bolinho:"))
onigi= float(input("quantidade de onigi:"))

total= (7.00 * ramem) + (6.00 * menma ) + (3.00 * bolinho) + (5.00 * onigi)

if (total > 42.00) :
   vf= total - (total * 0.1)
   print(round(vf,2),"ryous")
else:
   print(Round((total - 3),2),"ryous")

