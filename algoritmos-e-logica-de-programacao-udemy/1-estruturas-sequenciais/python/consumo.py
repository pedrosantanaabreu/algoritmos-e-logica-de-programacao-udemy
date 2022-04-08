"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais. 
"""

# Recebendo valores
distancia_percorrida = float(input("Distância percorrida (km) | "))
combustivel_gasto = float(input("Combustível gasto (L) | "))

# Calculando
consumo_medio = combustivel_gasto / distancia_percorrida

# Exibindo resultado
print("\nConsumo médio | {:.2f}".format(consumo_medio))
