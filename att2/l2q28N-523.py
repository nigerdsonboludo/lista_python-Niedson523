#Lista de Exercício 2 - Questão 28
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
                self.quantidade_carne = float(input("Digite a quantidade de carne em Kg: "))
                if self.quantidade_carne > 0:
                    break
                else:
                    print("Quantidade inválida. Digite um valor positivo.")
            except ValueError:
                print("Quantidade inválida. Digite um número válido.")

        while self.pagamento_cartao not in ["S", "N"]:
            self.pagamento_cartao = input("Pagamento com cartão Tabajara? (S - Sim, N - Não): ").upper()

    def calcular_valor_total(self):
        preco_file_duplo = 5.80
        preco_alcatra = 6.80
