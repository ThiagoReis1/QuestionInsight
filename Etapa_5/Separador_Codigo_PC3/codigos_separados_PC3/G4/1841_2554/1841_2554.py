from math import*
vq=float(input("valor inicial investido: "))
tr=float(input("taxa de rendimento: "))

y=(log(vq*3)-log(vq))/tr
print (int(round(y,1)))