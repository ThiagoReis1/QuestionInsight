classe_a = 80
classe_b = 50
classe_c = 30

#Ingressos vendidos
ing_a = int(input("Digite a quantidade de ingressos vendidos da Classe A"))

ing_b = int(input("Digite a quantidade de ingressos vendidos da Classe B"))

ing_c = int(input("Digite a quantidade de ingressos vendidos da Classe C"))

#Renda total
a = float(ing_a * classe_a)
b = float(ing_b * classe_b)
c = float(ing_c * classe_c)

print(a + b + c)
