"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem. 
"""

# Recebendo valores
coeficiente_a = float(input("Digite o coeficiente A | "))
coeficiente_b = float(input("Digite o coeficiente B | "))
coeficiente_c = float(input("Digite o coeficiente C | "))

# Calculando
delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

if delta >= 0:
    x1 = (-coeficiente_b + delta ** 0.5) / (coeficiente_a * 2)
    x2 = (-coeficiente_b - delta ** 0.5) / (coeficiente_a * 2)
    if delta == 0:
        x2 = x1
    print("\nDelta | {:.2f}\nX1 | {:.2f}\nX2 | {:.2f}".format(delta, x1, x2))
else:
    print("\nA equação não possui raízes reais")
