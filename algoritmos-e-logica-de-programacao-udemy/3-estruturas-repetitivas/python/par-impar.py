"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
apenas NULO.
"""

numeros_digitar = int(input("Quantos números você vai digitar | "))
for i in range(numeros_digitar):
    numero = int(input("Digite o {}º número | ".format(i + 1)))
    if numero > 0:
        if numero % 2 == 0:
            print("Par positivo")
        else:
            print("Impar positivo")
    elif numero < 0:
        if numero % 2 == 0:
            print("Par negativo")
        else:
            print("Impar negativo")
    else:
        print("Nulo")
