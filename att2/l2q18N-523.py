#Lista de Exercício 2 - Questão 18
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class DataValida:
    def __init__(self):
        self.data = ""

    def ler_data(self):
        while True:
            try:
                self.data = input("Digite uma data no formato dd/mm/aaaa: ")
                self.validar_data()
                break
            except ValueError as e:
                print(str(e))

    def validar_data(self):
        dia, mes, ano = map(int, self.data.split("/"))

        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido.")
        elif mes < 1 or mes > 12:
            raise ValueError("Mês inválido.")
        elif ano < 1:
            raise ValueError("Ano inválido.")
        elif mes in [4, 6, 9, 11] and dia > 30:
            raise ValueError("Dia inválido para o mês informado.")
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    raise ValueError("Dia inválido para o mês informado.")
            elif dia > 28:
                raise ValueError("Dia inválido para o mês informado.")

    def exibir_resultado(self):
        print("A data {} é válida.".format(self.data))


def main():
    data = DataValida()
    data.ler_data()
    data.exibir_resultado()


if __name__ == "__main__":
    main()
