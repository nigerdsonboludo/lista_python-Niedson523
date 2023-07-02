#Lista de Exercício 1 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

class Calculadora:
    def calcular_salario_mensal(self, valor_hora, horas_trabalhadas):
        return valor_hora * horas_trabalhadas


def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("Erro: O valor deve ser um número positivo ou zero.")
        except ValueError:
            print("Erro: O valor digitado não é válido.")


if __name__ == "__main__":
    calculadora = Calculadora()

    valor_hora = obter_valor("Digite o valor que você ganha por hora: ")
    horas_trabalhadas = obter_valor("Digite o número de horas trabalhadas no mês: ")

    salario_total = calculadora.calcular_salario_mensal(valor_hora, horas_trabalhadas)

    print(f"O total do seu salário no mês é: {salario_total}")
