#Lista de Exercício 2 - Questão 22
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ParOuImpar:
    def __init__(self):
        self.numero = 0

    def ler_numero(self):
        while True:
            try:
                self.numero = int(input("Digite um número inteiro: "))
                break
            except ValueError:
                print("Número inválido. Digite um número inteiro válido.")

    def verificar_paridade(self):
        if self.numero % 2 == 0:
            return "par"
        else:
            return "ímpar"

    def exibir_resultado(self):
        paridade = self.verificar_paridade()
        print("O número {} é {}.".format(self.numero, paridade))


def main():
    numero = ParOuImpar()
    numero.ler_numero()
    numero.exibir_resultado()


if __name__ == "__main__":
    main()
