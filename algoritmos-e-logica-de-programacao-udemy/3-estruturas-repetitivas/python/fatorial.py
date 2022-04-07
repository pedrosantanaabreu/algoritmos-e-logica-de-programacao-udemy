"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
fatorial de N.
"""

numero = int(input("Digite o valor de N | "))
fatorial = 1
for i in range(numero + 1):
    if i != 0:
        fatorial *= i
print("Fatorial | {}".format(fatorial))
