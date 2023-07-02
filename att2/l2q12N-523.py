#Lista de Exercício 2 - Questão 12
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class FolhaDePagamento:
    def __init__(self):
        self.valor_hora = 0
        self.horas_trabalhadas = 0

    def ler_dados(self):
        while True:
            try:
                self.valor_hora = float(input("Digite o valor da hora de trabalho: "))
                self.horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas

    def calcular_desconto_ir(self, salario_bruto):
        if salario_bruto <= 900:
            return 0
        elif salario_bruto <= 1500:
            return salario_bruto * 0.05
        elif salario_bruto <= 2500:
            return salario_bruto * 0.1
        else:
            return salario_bruto * 0.2

    def calcular_folha(self):
        self.ler_dados()

        salario_bruto = self.calcular_salario_bruto()
        desconto_ir = self.calcular_desconto_ir(salario_bruto)
        desconto_inss = salario_bruto * 0.1
        fgts = salario_bruto * 0.11

        total_descontos = desconto_ir + desconto_inss
        salario_liquido = salario_bruto - total_descontos

        print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
        print("(-) IR ({:.0f}%): R$ {:.2f}".format((desconto_ir / salario_bruto) * 100, desconto_ir))
        print("(-) INSS (10%): R$ {:.2f}".format(desconto_inss))
        print("FGTS (11%): R$ {:.2f}".format(fgts))
        print("Total de descontos: R$ {:.2f}".format(total_descontos))
        print("Salário Líquido: R$ {:.2f}".format(salario_liquido))


def main():
    folha = FolhaDePagamento()
    folha.calcular_folha()


if __name__ == "__main__":
    main()
