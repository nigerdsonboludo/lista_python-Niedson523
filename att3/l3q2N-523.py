#Lista de Exercício 3 - Questão 2
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ValorCombustivel:
    def __init__(self):
        self.litros_vendidos = 0
        self.tipo_combustivel = ""

    def ler_dados(self):
        while True:
            try:
                self.litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
                if 0 < self.litros_vendidos <= 1000:
                    break
                else:
                    print("Quantidade inválida. Digite um valor entre 0 e 1000.")
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

        while self.tipo_combustivel not in ["A", "G"]:
            self.tipo_combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()

    def calcular_valor_pago(self):
        preco_alcool = 1.90
        preco_gasolina = 2.50

        if self.tipo_combustivel == "A":
            if self.litros_vendidos <= 20:
                valor_pago = self.litros_vendidos * (preco_alcool - (0.03 * preco_alcool))
            else:
                valor_pago = self.litros_vendidos * (preco_alcool - (0.05 * preco_alcool))
        else:
            if self.litros_vendidos <= 20:
                valor_pago = self.litros_vendidos * (preco_gasolina - (0.04 * preco_gasolina))
            else:
                valor_pago = self.litros_vendidos * (preco_gasolina - (0.06 * preco_gasolina))

        return valor_pago

    def exibir_valor_pago(self):
        valor_pago = self.calcular_valor_pago()
        print("Valor a ser pago: R$ {:.2f}".format(valor_pago))


def main():
    combustivel = ValorCombustivel()
    combustivel.ler_dados()
    combustivel.exibir_valor_pago()


if __name__ == "__main__":
    main()
