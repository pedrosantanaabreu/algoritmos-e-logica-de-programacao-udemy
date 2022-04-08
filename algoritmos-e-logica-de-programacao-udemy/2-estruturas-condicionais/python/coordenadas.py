"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia os valores das coordenadas X e Y de um ponto no plano
cartesiano. A seguir, determine qual o quadrante ao qual pertence o
ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a
mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva
“Eixo X” ou “Eixo Y”, conforme for a situação. 
horas.
"""

# Recebendo valores
x = float(input("Digite o valor de X | "))
y = float(input("Digite o valor de Y | "))

# Calculando
if x > 0 and y > 0:
    print("\nQ1")
elif x < 0 and y > 0:
    print("\nQ2")
elif x < 0 and y < 0:
    print("\nQ3")
elif x > 0 and y < 0:
    print("\nQ4")
else:
    if x == 0 and y == 0:
        print("\nOrigem")
    elif x == 0:
        print("\nEixo X")
    else:
        print("\nEixo Y")
