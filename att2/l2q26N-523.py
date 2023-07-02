#Lista de Exercício 2 - Questão 26
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
                if self.litros_vendidos > 0:
                    break
                else:
                    print("Quantidade inválida. Digite um valor positivo.")
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

        while self.tipo_combustivel not in ["A", "G"]:
            self.tipo_combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()

    def calcular_valor(self):
        preco_alcool = 1.90
        preco_gasolina = 2.50

        if self.tipo_combustivel == "A":
            if self.litros_vendidos <= 20:
                desconto = self.litros_vendidos * 0.03
            else:
                desconto = self.litros_vendidos * 0.05
            valor_total = self.litros_vendidos * (preco_alcool - desconto)
        else:
            if self.litros_vendidos <= 20:
                desconto = self.litros_vendidos * 0.04
            else:
                desconto = self.litros_vendidos * 0.06
            valor_total = self.litros_vendidos * (preco_gasolina - desconto)

        return valor_total

    def exibir_resultado(self):
        valor_total = self.calcular_valor()
        print("Valor a ser pago: R$ {:.2f}".format(valor_total))


def main():
    combustivel = ValorCombustivel()
    combustivel.ler_dados()
    combustivel.exibir_resultado()


if __name__ == "__main__":
    main()
