"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler a quantidade de glicose
no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de
referência ao lado. 
"""

# Recebendo valores
glicose = float(input("Digite a medida da glicose | "))

# Calculando
if glicose > 100:
    if glicose > 140:
        print("\nClassificação | Diabetes")
    else:
        print("\nClassificação | Elevado")
else:
    print("\nClassificação | Normal")
