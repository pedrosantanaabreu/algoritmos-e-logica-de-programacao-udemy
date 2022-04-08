"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior. 
"""

# Recebendo valores
distancia_1 = float(input("Digite o 1ª distância | "))
distancia_2 = float(input("Digite o 2ª distância | "))
distancia_3 = float(input("Digite o 3ª distância | "))

# Calculando
maior = distancia_1
if distancia_2 > maior:
    menor = distancia_2
if distancia_3 > maior:
    menor = distancia_3

# Exibindo resultado
print("\nA maior distância | {:.2f}".format(maior))
