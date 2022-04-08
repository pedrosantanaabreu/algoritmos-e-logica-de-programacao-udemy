"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
números lidos. Em caso de empate, mostrar apenas uma vez.
"""

# Recebendo valores
numero_1 = int(input("Digite o 1ª número | "))
numero_2 = int(input("Digite o 2ª número | "))
numero_3 = int(input("Digite o 3ª número | "))

# Calculando
menor = numero_1
if numero_2 < menor:
    menor = numero_2
if numero_3 < menor:
    menor = numero_3

# Exibindo resultado
print("\nO menor número | {}".format(menor))
