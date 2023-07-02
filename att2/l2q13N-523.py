#Lista de Exercício 2 - Questão 13
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class DiaDaSemana:
    def __init__(self):
        self.numero_dia = 0

    def ler_numero_dia(self):
        while True:
            try:
                self.numero_dia = int(input("Digite um número de 1 a 7 para representar o dia da semana: "))
                if 1 <= self.numero_dia <= 7:
                    break
                else:
                    print("Valor inválido. Digite um número entre 1 e 7.")
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def exibir_dia_semana(self):
        dias_semana = {
            1: "Domingo",
            2: "Segunda-feira",
            3: "Terça-feira",
            4: "Quarta-feira",
            5: "Quinta-feira",
            6: "Sexta-feira",
            7: "Sábado"
        }

        dia_semana = dias_semana[self.numero_dia]
        print("O número {} corresponde ao dia {}.".format(self.numero_dia, dia_semana))


def main():
    dia = DiaDaSemana()
    dia.ler_numero_dia()
    dia.exibir_dia_semana()


if __name__ == "__main__":
    main()
