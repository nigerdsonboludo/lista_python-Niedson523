#Lista de Exercício 2 - Questão 17
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class AnoBissexto:
    def __init__(self):
        self.ano = 0

    def ler_ano(self):
        while True:
            try:
                self.ano = int(input("Digite o ano: "))
                break
            except ValueError:
                print("Ano inválido. Digite um número válido.")

    def verificar_bissexto(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            return True
        else:
            return False

    def exibir_resultado(self):
        if self.verificar_bissexto():
            print("O ano {} é bissexto.".format(self.ano))
        else:
            print("O ano {} não é bissexto.".format(self.ano))


def main():
    ano = AnoBissexto()
    ano.ler_ano()
    ano.exibir_resultado()


if __name__ == "__main__":
    main()
