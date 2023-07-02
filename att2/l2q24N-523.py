#Lista de Exercício 2 - Questão 24
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class OperacoesNumero:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0

    def ler_numeros(self):
        while True:
            try:
                self.numero1 = float(input("Digite o primeiro número: "))
                self.numero2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Número inválido. Digite números válidos.")

    def verificar_paridade(self, numero):
        if numero % 2 == 0:
            return "par"
        else:
            return "ímpar"

    def verificar_positividade(self, numero):
        if numero > 0:
            return "positivo"
        elif numero < 0:
            return "negativo"
        else:
            return "neutro"

    def verificar_tipo(self, numero):
        if numero.is_integer():
            return "inteiro"
        else:
            return "decimal"

    def realizar_operacoes(self):
        resultado = self.numero1 + self.numero2
        print("Soma: {:.2f}".format(resultado))

        resultado = self.numero1 - self.numero2
        print("Subtração: {:.2f}".format(resultado))

        resultado = self.numero1 * self.numero2
        print("Multiplicação: {:.2f}".format(resultado))

        if self.numero2 != 0:
            resultado = self.numero1 / self.numero2
            print("Divisão: {:.2f}".format(resultado))
        else:
            print("Divisão por zero não é permitida.")

        tipo1 = self.verificar_tipo(self.numero1)
        tipo2 = self.verificar_tipo(self.numero2)
        print("Primeiro número é {}, segundo número é {}.".format(tipo1, tipo2))

        paridade1 = self.verificar_paridade(self.numero1)
        paridade2 = self.verificar_paridade(self.numero2)
        print("Primeiro número é {}, segundo número é {}.".format(paridade1, paridade2))

        positividade1 = self.verificar_positividade(self.numero1)
        positividade2 = self.verificar_positividade(self.numero2)
        print("Primeiro número é {}, segundo número é {}.".format(positividade1, positividade2))


def main():
    numeros = OperacoesNumero()
    numeros.ler_numeros()
    numeros.realizar_operacoes()


if __name__ == "__main__":
    main()

