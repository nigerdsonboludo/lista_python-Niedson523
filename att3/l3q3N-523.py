#Lista de Exercício 3 - Questão 3
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
                self.quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
                self.quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))
                break
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

    def calcular_valor_pago(self):
        preco_morango = 2.50
        preco_maca = 1.80
        limite_desconto = 8
        valor_total = 0

        if self.quantidade_morangos <= 5:
            valor_morango = self.quantidade_morangos * preco_morango
        else:
            valor_morango = self.quantidade_morangos * (preco_morango - 0.30)

        if self.quantidade_macas <= 5:
            valor_maca = self.quantidade_macas * preco_maca
        else:
            valor_maca = self.quantidade_macas * (preco_maca - 0.30)

        valor_total = valor_morango + valor_maca

        if self.quantidade_morangos + self.quantidade_macas > limite_desconto or valor_total > 25.00:
            valor_total *= 0.90

        return valor_total

    def exibir_valor_pago(self):
        valor_pago = self.calcular_valor_pago()
        print("Valor a ser pago: R$ {:.2f}".format(valor_pago))


def main():
    frutas = ValorFrutas()
    frutas.ler_dados()
    frutas.exibir_valor_pago()


if __name__ == "__main__":
    main()
