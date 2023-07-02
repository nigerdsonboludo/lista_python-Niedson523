#Lista de Exercício 2 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Comparador:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def encontrar_maior(self):
        maior = max(self.num1, self.num2, self.num3)
        return maior

    def encontrar_menor(self):
        menor = min(self.num1, self.num2, self.num3)
        return menor

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    comparador = Comparador(num1, num2, num3)
    maior_numero = comparador.encontrar_maior()
    menor_numero = comparador.encontrar_menor()

    print("O maior número é:", maior_numero)
    print("O menor número é:", menor_numero)

except ValueError:
    print("Erro: digite apenas números.")
