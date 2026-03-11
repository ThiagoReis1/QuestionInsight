B=float(input("Qual o comprimento da base maior?"))
b=float(input("Qual o comprimento da base menor?"))
h=float(input("Qual o comprimento da altura?"))
custo_fertilizante=float(input("Qual o custo do fertilizante por metro quadrado?"))
area=h*(B+b)/2
custo_final=area*custo_fertilizante
print(round(custo_final,2))