"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais, conforme exemplo. 
"""

# Recebendo valores
largura = float(input("Digite a largura do terreno | "))
comprimento = float(input("Digite o comprimento do terreno | "))
valor_m2 = float(input("Digite o valor do metro quadrado | R$ "))

# Calculando
area = largura * comprimento
preco_terreno = area * valor_m2

# Exibindo resultado
print("\nÁrea do terreno | {:.2f} m2\nPreço do terreno | R$ {:.2f}".format(area, preco_terreno))
