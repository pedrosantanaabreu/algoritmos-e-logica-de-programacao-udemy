"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
encerrado. Considere que a senha correta é o valor 2002. 
"""

senha_usuario = int(input("Digite a senha | "))
SENHA_FIXA = 2002
while True:
    if senha_usuario == SENHA_FIXA:
        print("\nAcesso permitido!")
        break
    else:
        senha_usuario = int(input("Senha invalida! Tente novamente | "))
