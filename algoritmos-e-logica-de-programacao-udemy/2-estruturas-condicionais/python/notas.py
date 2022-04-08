"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
mensagem "REPROVADO", conforme exemplos.
"""

# Recebendo valores
nota_1 = float(input("Digite a 1ª nota | "))
nota_2 = float(input("Digite a 2ª nota | "))

# Calculando
nota_final = nota_1 + nota_2

# Exibindo resultado
print("\nNota final | {:.1f}".format(nota_final))
if nota_final < 60:
    print("Reprovado")
