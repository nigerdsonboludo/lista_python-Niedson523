#Lista de Exercício 2 - Questão 23
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class InteiroOuDecimal:
    def __init__(self):
        self.numero = 0

    def ler_numero(self):
        while True:
            try:
                self.numero = float(input("Digite um número: "))
                break
            except ValueError:
                print("Número inválido. Digite um número válido.")

    def verificar_tipo(self):
        if self.numero.is_integer():
            return "inteiro"
        else:
            return "decimal"

    def exibir_resultado(self):
        tipo = self.verificar_tipo()
        print("O número {} é {}.".format(self.numero, tipo))


def main():
    numero = InteiroOuDecimal()
    numero.ler_numero()
    numero.exibir_resultado()


if __name__ == "__main__":
    main()
