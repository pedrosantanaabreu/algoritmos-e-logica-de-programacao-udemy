"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os
números podem ser digitados em qualquer ordem.
"""

# Recebendo valores
numero_1 = int(input("Digite o 1º número | "))
numero_2 = int(input("Digite o 2º número | "))

# Calculando
if numero_1 % numero_2 == 0:
    print("\nSão múltiplos")
else:
    print("\nNão são múltiplos")
