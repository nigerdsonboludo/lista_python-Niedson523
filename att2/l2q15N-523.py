#Lista de Exercício 2 - Questão 15
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Triangulo:
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0

    def ler_lados(self):
        while True:
            try:
                self.lado1 = float(input("Digite o valor do primeiro lado: "))
                self.lado2 = float(input("Digite o valor do segundo lado: "))
                self.lado3 = float(input("Digite o valor do terceiro lado: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def verificar_triangulo(self):
        if (self.lado1 + self.lado2 > self.lado3) and (self.lado1 + self.lado3 > self.lado2) and (self.lado2 + self.lado3 > self.lado1):
            return True
        else:
            return False

    def obter_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def exibir_resultado(self):
        if self.verificar_triangulo():
            tipo_triangulo = self.obter_tipo_triangulo()
            print("Os valores podem formar um triângulo {}.".format(tipo_triangulo))
        else:
            print("Os valores não podem formar um triângulo.")


def main():
    triangulo = Triangulo()
    triangulo.ler_lados()
    triangulo.exibir_resultado()


if __name__ == "__main__":
    main()

