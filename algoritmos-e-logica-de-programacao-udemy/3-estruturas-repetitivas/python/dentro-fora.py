"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
conforme exemplo
"""

dentro = 0
fora = 0
numeros_digitar = int(input("Quantos números você vai digitar | "))
for i in range(numeros_digitar):
    numero = int(input("Digite o {}º número | ".format(i + 1)))
    if numero >= 10 and numero <= 20:
        dentro += 1
    else:
        fora += 1
print("\nDentro | {}\nFora | {}".format(dentro, fora))
