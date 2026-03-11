from math import*
snowberry= ((5**(1/2))-1)/4
sfogo= (5-2*(5**0.5))**(1/2)
amanita= 5*(5-(2*(5**0.5)))
quantp= float(input("Diga a quantidade de porções :"))
qd= quantp*snowberry #qd é abreviação de quantidade snowberry
qs= quantp*sfogo
qa= quantp*amanita
print(round(qd,2))
print(round(qs,2))
print(round(qa,2))