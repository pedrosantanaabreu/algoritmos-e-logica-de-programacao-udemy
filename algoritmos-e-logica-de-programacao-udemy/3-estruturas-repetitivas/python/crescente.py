"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados dois valores iguais. 
"""

print("Digite dois números")
while True:
    numero_1 = int(input(""))
    numero_2 = int(input(""))
    if numero_1 < numero_2:
        print("\nCrescente")
    elif numero_1 > numero_2:
        print("\nDecrescente")
    else:
        break
    
    print("\nDigite outros dois números")
