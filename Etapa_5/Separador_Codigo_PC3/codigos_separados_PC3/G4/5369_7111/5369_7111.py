from numpy import *
v = array (eval(input("digite os nove digitos do cpf:")))
vet_ax= [9,8,7,6,5,4,3,2,1]

c1= v[0] * vet_ax[0]
c2= v[1] * vet_ax[1]
c3= v[2] * vet_ax[2]
c4= v[3] * vet_ax[3]
c5= v[4] * vet_ax[4]
c6= v[5] * vet_ax[5]
c7= v[6] * vet_ax[6]
c8= v[7] * vet_ax[7]
c9= v[8] * vet_ax[8]
total_soma= c1+c2+c3+c4+c5+c6+c7+c8+c9
rest= total_soma%11
print(rest)
