#Lista de Exercício 2 - Questão 16
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import math

class EquacaoSegundoGrau:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def ler_coeficientes(self):
        while True:
            try:
                self.a = float(input("Digite o valor de a: "))
                if self.a != 0:
                    break
                else:
                    print("O valor de a deve ser diferente de zero.")
            except ValueError:
                print("Valor inválido. Digite um número válido.")

        while True:
            try:
                self.b = float(input("Digite o valor de b: "))
                self.c = float(input("Digite o valor de c: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def calcular_delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def calcular_raizes(self):
        delta = self.calcular_delta()

        if delta < 0:
            return None
        elif delta == 0:
            raiz = -self.b / (2 * self.a)
            return raiz
        else:
            raiz1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return raiz1, raiz2

    def exibir_resultado(self):
        if self.a == 0:
            print("A equação não é do segundo grau.")
            return

        raizes = self.calcular_raizes()

        if raizes is None:
            print("A equação não possui raízes reais.")
        elif isinstance(raizes, float):
            print("A equação possui uma raiz real: {:.2f}".format(raizes))
        else:
            print("A equação possui duas raízes reais: {:.2f} e {:.2f}".format(raizes[0], raizes[1]))


def main():
    equacao = EquacaoSegundoGrau()
    equacao.ler_coeficientes()
    equacao.exibir_resultado()


if __name__ == "__main__":
    main()
