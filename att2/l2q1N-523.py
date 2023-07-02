#Lista de Exercício 2 - Questão 1
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ComparadorNumeros:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def obter_maior(self):
        if self.numero1 > self.numero2:
            return self.numero1
        else:
            return self.numero2


def obter_valor_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")


def main():
    numero1 = obter_valor_numerico("Digite o primeiro número: ")
    numero2 = obter_valor_numerico("Digite o segundo número: ")

    comparador = ComparadorNumeros(numero1, numero2)
    maior_numero = comparador.obter_maior()

    print(f"O maior número é: {maior_numero}")


if __name__ == '__main__':
    main()
