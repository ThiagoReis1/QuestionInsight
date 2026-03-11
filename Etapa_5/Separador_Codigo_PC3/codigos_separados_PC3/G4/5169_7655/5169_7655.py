p= float(input("Insira o peso (em gramas) do saco de racao: "))
qtd= float(input("Insira a quantidade diaria de racao: "))

#Saida
qf= p-(qtd*4)
print(round(qf,2))