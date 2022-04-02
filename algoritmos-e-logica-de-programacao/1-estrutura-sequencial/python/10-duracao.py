"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos
"""

# Recebendo valores
segundos = int(input("Digite o tempo sem segundos | "))

# Calculando
minutos = segundos // 60 % 60
horas = segundos // 60 // 60
segundos = segundos % 60

# Exibindo resultado
print("\n{}:{}:{}".format(horas, minutos, segundos))
