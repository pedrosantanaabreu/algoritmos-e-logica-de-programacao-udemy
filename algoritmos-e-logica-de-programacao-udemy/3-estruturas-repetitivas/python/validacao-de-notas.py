"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
intervalo [0,10]). Cada nota deve ser validada separadamente.
"""

soma_notas = 0
media = 0
for i in range(1, 3):
    nota = float(input("Digite a {}ª nota | ".format(i)))
    while nota < 0 or nota > 10:
        nota = float(input("Valor invalido! Tente novamente | "))
    soma_notas += nota

media = soma_notas / 2
print("Média | {:.2f}".format(media))
