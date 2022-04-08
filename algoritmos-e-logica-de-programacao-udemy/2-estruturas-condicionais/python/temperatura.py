"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com 
"""

# Recebendo valores
temperatura_celsius = float(input("Digite a temperatura em celsius | "))

# Calculando
temperatura_fahrenheit = 180 * temperatura_celsius / 100 + 32

# Exibindo resultado
print("\nA temperatura em Fahrenheit será | {:.1f} °F".format(temperatura_fahrenheit))
