"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
"""

# Recebendo valores
base = float(input("Digite a base do retângulo | "))
altura = float(input("Digite a altura do retângulo | "))

# Calculando
area = base * altura
perimetro = 2 * (base + altura) 
diagonal = (base ** 2 + altura ** 2) ** 0.5

# Exibindo resultado
print("\nÁrea | {:.2f}\nPerímetro | {:.2f}\nDiagonal | {:.2f}".format(area, perimetro, diagonal))
