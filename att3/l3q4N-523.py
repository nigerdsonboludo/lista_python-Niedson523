#Lista de Exercício 3 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class CupomFiscal:
    def __init__(self):
        self.tipo_carne = ""
        self.quantidade_carne = 0
        self.pagamento_cartao = ""

    def ler_dados(self):
        while self.tipo_carne not in ["F", "A", "P"]:
            self.tipo_carne = input("Digite o tipo de carne (F - Filé Duplo, A - Alcatra, P - Picanha): ").upper()

        while True:
            try:
                self.quantidade_carne = float(input("Digite a quantidade de carne (em Kg): "))
                break
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

        while self.pagamento_cartao not in ["S", "N"]:
            self.pagamento_cartao = input("Pagamento com cartão Tabajara? (S - Sim, N - Não): ").upper()

    def calcular_valor_total(self):
        preco_file_duplo = 5.80
        preco_alcatra = 6.80
        preco_picanha = 7.80
        desconto_cartao = 0.05

        if self.tipo_carne == "F":
            preco_carne = preco_file_duplo
        elif self.tipo_carne == "A":
            preco_carne = preco_alcatra
        else:
            preco_carne = preco_picanha

        valor_total = self.quantidade_carne * preco_carne

        if self.pagamento_cartao == "S":
            valor_desconto = valor_total * desconto_cartao
            valor_total -= valor_desconto

        return valor_total

    def exibir_cupom_fiscal(self):
        valor_total = self.calcular_valor_total()
        print("Cupom Fiscal:")
        print("Tipo de carne: {}".format(self.tipo_carne))
        print("Quantidade de carne: {:.2f} Kg".format(self.quantidade_carne))
        print("Preço total: R$ {:.2f}".format(valor_total))
        print("Pagamento: Cartão Tabajara" if self.pagamento_cartao == "S" else "Pagamento: Outro método")


def main():
    cupom = CupomFiscal()
    cupom.ler_dados()
    cupom.exibir_cupom_fiscal()


if __name__ == "__main__":
    main()
