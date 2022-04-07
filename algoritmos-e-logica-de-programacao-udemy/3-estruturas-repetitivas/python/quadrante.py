"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
escrever mensagem alguma).
"""

while True:
    print("Digite os valores das coordenadas X e Y:")
    x = int(input())
    y = int(input())
    if x > 0 and y > 0:
        print("\nQ1")
    elif x < 0 and y > 0:
        print("\nQ2")
    elif x < 0 and y < 0:
        print("\nQ3")
    elif x > 0 and y < 0:
        print("\nQ4")
    else:
        break
