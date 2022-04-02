"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
números.
"""

# Recebendo valores
numero_1 = int(input("Digite o 1º número | "))
numero_2 = int(input("Digite o 2º número | "))

# Calculando
soma = numero_1 + numero_2

# Exibindo resultado
print("\nResultado | {} + {} = {}".format(numero_1, numero_2, soma))
