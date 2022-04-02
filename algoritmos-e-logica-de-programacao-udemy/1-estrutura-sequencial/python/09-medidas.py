"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
"""

# Recebendo valores
medida_1 = float(input("Digite a 1ª medida | "))
medida_2 = float(input("Digite a 2ª medida | "))
medida_3 = float(input("Digite a 3ª medida | "))

# Calculando
area_quadrado = medida_1 ** 2
area_triangulo = medida_1 * medida_2 / 2
area_trapezio = (medida_1 + medida_2) * medida_3 / 2

# Exibindo resultado
print("\nÁrea quadrado | {:.2f}\nÁrea triângulo | {:.2f}\nÁrea trapézio {:.2f}".format(area_quadrado, area_triangulo, area_trapezio))
