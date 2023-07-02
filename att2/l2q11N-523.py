#Lista de Exercício 2 - Questão 11
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class TabajaraOrganizations:
    def __init__(self):
        self.salario_atual = 0

    def ler_salario_atual(self):
        while True:
            try:
                self.salario_atual = float(input("Digite o salário atual do colaborador: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def calcular_reajuste(self):
        percentual_aumento = 0
        if self.salario_atual <= 280:
            percentual_aumento = 20
        elif self.salario_atual <= 700:
            percentual_aumento = 15
        elif self.salario_atual <= 1500:
            percentual_aumento = 10
        else:
            percentual_aumento = 5

        aumento = self.salario_atual * (percentual_aumento / 100)
        novo_salario = self.salario_atual + aumento

        print("Salário antes do reajuste: R$ {:.2f}".format(self.salario_atual))
        print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
        print("Valor do aumento: R$ {:.2f}".format(aumento))
        print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))


def main():
    org_tabajara = TabajaraOrganizations()
    org_tabajara.ler_salario_atual()
    org_tabajara.calcular_reajuste()


if __name__ == "__main__":
    main()
