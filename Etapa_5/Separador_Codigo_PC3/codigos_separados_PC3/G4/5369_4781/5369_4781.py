

cpf = eval(input())

v = [9,8,7,6,5,4,3,2,1]

a = (cpf[0] * v[0])
b = (cpf[1] * v[1])
c = (cpf[2] * v[2])
d = (cpf[3] * v[3])
e = (cpf[4] * v[4])
f = (cpf[5] * v[5])
g = (cpf[6] * v[6])
h = (cpf[7] * v[7])
i = (cpf[8] * v[8])



total_soma = a+b+c+d+e+f+g+h+i
z = total_soma % 11
print(z)