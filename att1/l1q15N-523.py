#Lista de Exercício 1 - Questão 15
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class CalculadoraSalario:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas

    def calcular_desconto_ir(self, salario_bruto):
        return salario_bruto * 0.11

    def calcular_desconto_inss(self, salario_bruto):
        return salario_bruto * 0.08

    def calcular_desconto_sindicato(self, salario_bruto):
        return salario_bruto * 0.05

    def calcular_salario_liquido(self):
        salario_bruto = self.calcular_salario_bruto()
        desconto_ir = self.calcular_desconto_ir(salario_bruto)
        desconto_inss = self.calcular_desconto_inss(salario_bruto)
        desconto_sindicato = self.calcular_desconto_sindicato(salario_bruto)

        salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
        return salario_liquido


def obter_valor_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")


def main():
    valor_hora = obter_valor_numerico("Qual o valor que você ganha por hora? ")
    horas_trabalhadas = obter_valor_numerico("Quantas horas você trabalhou no mês? ")

    calculadora = CalculadoraSalario(valor_hora, horas_trabalhadas)

    salario_bruto = calculadora.calcular_salario_bruto()
    desconto_ir = calculadora.calcular_desconto_ir(salario_bruto)
    desconto_inss = calculadora.calcular_desconto_inss(salario_bruto)
    desconto_sindicato = calculadora.calcular_desconto_sindicato(salario_bruto)
    salario_liquido = calculadora.calcular_salario_liquido()

    print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
    print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
    print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
    print(f"\nSalário Líquido: R$ {salario_liquido:.2f}")


if __name__ == '__main__':
    main()
