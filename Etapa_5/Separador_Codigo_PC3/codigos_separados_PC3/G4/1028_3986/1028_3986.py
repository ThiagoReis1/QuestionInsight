vol=float(input("volume da agua consumida: "))
f=15.0
icms=0.35
cus=0.37
vp=(((vol * cus) + f ) * icms) 
total=vp + f + (vol * cus)

print(round(total,2))