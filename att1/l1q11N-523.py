#Lista de Exercício 1 - Questão 11
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#o produto do dobro do primeiro com metade do segundo 
#a soma do triplo do primeiro com o terceiro. 
#o terceiro elevado ao cubo

class Calculadora:
    def calcular_produto(self, num1, num2):
        return (2 * num1) * (num2 / 2)

    def calcular_soma(self, num1, num3):
        return (3 * num1) + num3

    def calcular_cubo(self, num3):
        return num3 ** 3


def obter_numero_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Erro: O valor digitado não é um número inteiro válido.")


def obter_numero_real(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Erro: O valor digitado não é um número real válido.")


if __name__ == "__main__":
    calculadora = Calculadora()

    num1 = obter_numero_inteiro("Digite o primeiro número inteiro: ")
    num2 = obter_numero_inteiro("Digite o segundo número inteiro: ")
    num3 = obter_numero_real("Digite o número real: ")

    produto = calculadora.calcular_produto(num1, num2)
    soma = calculadora.calcular_soma(num1, num3)
    cubo = calculadora.calcular_cubo(num3)

    print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
    print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
    print(f"O terceiro elevado ao cubo é: {cubo}")
