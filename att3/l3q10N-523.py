#Lista de Exercício 3 - Questão 10
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Numeros:
    def gerar_numeros_intervalo(self, num1, num2):
        if num1 > num2:
            num1, num2 = num2, num1
        for i in range(num1, num2 + 1):
            print(i)

numeros = Numeros()
try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numeros.gerar_numeros_intervalo(numero1, numero2)
except ValueError:
    print("Valor inválido. Digite um número inteiro válido.")
