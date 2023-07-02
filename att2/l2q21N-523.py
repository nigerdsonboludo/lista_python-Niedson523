#Lista de Exercício 2 - Questão 21
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class CaixaEletronico:
    def __init__(self):
        self.valor_saque = 0

    def ler_valor_saque(self):
        while True:
            try:
                self.valor_saque = int(input("Digite o valor do saque (entre R$10 e R$600): "))
                if self.valor_saque >= 10 and self.valor_saque <= 600:
                    break
                else:
                    print("Valor inválido. Digite um valor entre R$10 e R$600.")
            except ValueError:
                print("Valor inválido. Digite um valor válido.")

    def calcular_notas(self):
        notas_disponiveis = [100, 50, 10, 5, 1]
        notas_quantidade = []

        valor_restante = self.valor_saque
        for nota in notas_disponiveis:
            quantidade = valor_restante // nota
            valor_restante -= quantidade * nota
            notas_quantidade.append(quantidade)

        return notas_quantidade

    def exibir_resultado(self):
        notas_quantidade = self.calcular_notas()

        print("Notas fornecidas:")
        notas_disponiveis = [100, 50, 10, 5, 1]
        for nota, quantidade in zip(notas_disponiveis, notas_quantidade):
            if quantidade > 0:
                print("{} nota(s) de R${}".format(quantidade, nota))


def main():
    caixa = CaixaEletronico()
    caixa.ler_valor_saque()
    caixa.exibir_resultado()


if __name__ == "__main__":
    main()
