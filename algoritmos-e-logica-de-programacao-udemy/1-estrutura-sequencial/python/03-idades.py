"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo. 
"""

# Recebendo valores
nome_1 = input("Dados da 1ª pessoa\nNome | ")
idade_1 = int(input("Idade | "))
nome_2 = input("\nDados da 2ª pessoa\nNome | ")
idade_2 = int(input("Idade | "))

# Calculando
media = (idade_1 + idade_2) / 2

# Exibindo resultado
print("\nA idade média de {} e {} é de {:.2f}".format(nome_1, nome_2, media))
