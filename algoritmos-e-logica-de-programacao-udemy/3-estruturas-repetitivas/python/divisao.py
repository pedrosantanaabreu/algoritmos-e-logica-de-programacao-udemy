"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”. 
"""

casos = int(input("Quantos casos você vai digitar | "))
for i in range(casos):
    print("Digite as informações do {}º caso".format(i + 1))
    numerador = float(input("Entre com o numerador | ")) 
    denominador = float(input("Entre com o denominador | "))
    if denominador != 0:
        divisao = numerador / denominador
        print("\nDivisão | {:.2f}".format(divisao))
    else:
        print("\nDivisão impossivel")
