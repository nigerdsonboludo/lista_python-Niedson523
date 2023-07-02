#Lista de Exercício 2 - Questão 27
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ValorFrutas:
    def __init__(self):
        self.quantidade_morangos = 0
        self.quantidade_macas = 0

    def ler_dados(self):
        while True:
            try:
                self.quantidade_morangos = float(input("Digite a quantidade em Kg de morangos: "))
                if self.quantidade_morangos >= 0:
                    break
                else:
                    print("Quantidade inválida. Digite um valor não negativo.")
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

        while True:
            try:
                self.quantidade_macas = float(input("Digite a quantidade em Kg de maçãs: "))
                if self.quantidade_macas >= 0:
                    break
                else:
                    print("Quantidade inválida. Digite um valor não negativo.")
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

    def calcular_valor(self):
        preco_morango = 2.50
        preco_maca = 1.80

        if self.quantidade_morangos <= 5:
            valor_morangos = self.quantidade_morangos * preco_morango
        else:
            valor_morangos = self.quantidade_morangos * 2.20

        if self.quantidade_macas <= 5:
            valor_macas = self.quantidade_macas * preco_maca
        else:
            valor_macas = self.quantidade_macas * 1.50

        valor_total = valor_morangos + valor_macas

        if (self.quantidade_morangos + self.quantidade_macas) > 8 or valor_total > 25:
            valor_total *= 0.9

        return valor_total

    def exibir_resultado(self):
        valor_total = self.calcular_valor()
        print("Valor a ser pago: R$ {:.2f}".format(valor_total))


def main():
    frutas = ValorFrutas()
    frutas.ler_dados()
    frutas.exibir_resultado()


if __name__ == "__main__":
    main()
