"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
mostrar a mensagem "IMPOSSIVEL CALCULAR". 
"""

# Recebendo valores
print("Digite as idades")
media = 0
quantidade_idades = 0
soma_idades = 0

while True:
    idade = int(input(""))
    if idade < 0:
        if quantidade_idades == 0:
            print("\nImpossivel calcular")
        else:
            media = soma_idades / quantidade_idades
            print("\nMédia | {:.2f}".format(media))
        break
    else:
        quantidade_idades += 1
        soma_idades += idade
