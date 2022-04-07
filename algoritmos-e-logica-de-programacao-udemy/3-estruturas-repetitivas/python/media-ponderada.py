"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
pela soma dos pesos. 
"""

casos = int(input("Quantos casos você vai digitar | "))
for i in range(casos):
    print("Digite as 3 notas do {}º caso".format(i + 1))
    nota_1 = float(input()) * 2
    nota_2 = float(input()) * 3
    nota_3 = float(input()) * 5
    media = (nota_1 + nota_2 + nota_3) / 10
    print("\nMedia | {:.1f}".format(media))
