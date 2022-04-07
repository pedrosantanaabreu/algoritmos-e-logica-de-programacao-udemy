"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
impares entre eles. 
"""

print("Digite dois números")
numero_1 = int(input())
numero_2 = int(input())
soma = 0
if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1
for i in range(numero_1, numero_2):
    if i % 2 != 0:
        soma += i
print("\nSoma | {}".format(abs(soma)))
