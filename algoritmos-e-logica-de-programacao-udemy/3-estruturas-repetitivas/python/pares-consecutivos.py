"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X
for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X
, se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a
soma de 12+14+16+18+20.
"""

while True:
    numero = int(input("Digite um numero inteiro | "))
    contador_numero = 0
    soma = 0
    if numero != 0:
        while contador_numero != 5:
            if numero % 2 == 0:
                contador_numero += 1
                soma += numero
            numero += 1
        print("Soma | {}".format(soma))
    else:
        break
