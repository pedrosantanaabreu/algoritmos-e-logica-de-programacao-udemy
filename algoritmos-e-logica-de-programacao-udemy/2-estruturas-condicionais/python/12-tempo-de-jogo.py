"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
horas.
"""

# Recebendo valores
hora_inicio = int(input("Digite a hora inicial | "))
hora_final = int(input("Digite a hora final | "))

# Calculando
if hora_inicio < hora_final:
    tempo_de_jogo = hora_final - hora_inicio
elif hora_inicio > hora_final:
    tempo_de_jogo = 24 - (hora_inicio - hora_final)
else:
    tempo_de_jogo = 24

# Exibindo resultado
print("\nO jogo durou {} hora(s)".format(tempo_de_jogo))
