"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo
"""

numero = int(input("Digite o número da tabuada | "))
for i in range(11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
