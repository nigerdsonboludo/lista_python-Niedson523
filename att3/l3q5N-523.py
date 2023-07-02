#Lista de Exercício 3 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Populacao:
    def __init__(self):
        self.populacao_A = 0
        self.populacao_B = 0
        self.taxa_crescimento_A = 0
        self.taxa_crescimento_B = 0

    def ler_dados(self):
        while True:
            try:
                self.populacao_A = int(input("Informe a população A: "))
                self.populacao_B = int(input("Informe a população B: "))
                self.taxa_crescimento_A = float(input("Informe a taxa de crescimento da população A (%): "))
                self.taxa_crescimento_B = float(input("Informe a taxa de crescimento da população B (%): "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def calcular_anos(self):
        anos = 0
        while self.populacao_A <= self.populacao_B:
            self.populacao_A *= 1 + self.taxa_crescimento_A / 100
            self.populacao_B *= 1 + self.taxa_crescimento_B / 100
            anos += 1
        return anos

    def exibir_resultado(self):
        anos = self.calcular_anos()
        print("Após {} anos, a população A ultrapassará a população B.".format(anos))


def main():
    continuar = True
    while continuar:
        populacao = Populacao()
        populacao.ler_dados()
        populacao.exibir_resultado()
        opcao = input("Deseja realizar outra operação? (S/N): ")
        if opcao.upper() != "S":
            continuar = False


if __name__ == "__main__":
    main()
