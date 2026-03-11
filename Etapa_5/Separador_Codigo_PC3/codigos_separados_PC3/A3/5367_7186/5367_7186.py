from numpy import*

c = array(eval(input("Digite o cpf: ")))
extra = [1,2,3,4,5,6,7,8,9]

total = (c[0]*1) + (c[1]*2) + (c[2]*3) + (c[3]*4) + (c[4]*5) + (c[5]*6) + (c[6]*7) + (c[7]*8) + (c[8]*9)
total_soma = total%11
print(total_soma)