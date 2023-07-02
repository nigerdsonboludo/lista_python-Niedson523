#Lista de Exercício 1 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math


class Calculadora:
    def calcular_area_circulo(self, raio):
        return math.pi * raio**2


def obter_raio(mensagem):
    while True:
        try:
            raio = float(input(mensagem))
            if raio >= 0:
                return raio
            else:
                print("Erro: O raio deve ser um valor positivo ou zero.")
        except ValueError:
            print("Erro: O valor digitado não é um raio válido.")


if __name__ == "__main__":
    calculadora = Calculadora()

    raio = obter_raio("Digite o raio do círculo: ")

    area = calculadora.calcular_area_circulo(raio)
    print(f"A área do círculo é: {area}")
