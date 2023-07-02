#Lista de Exercício 2 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class MaiorNumero:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0

    def obter_numeros(self):
        while True:
            try:
                self.num1 = float(input("Digite o primeiro número: "))
                self.num2 = float(input("Digite o segundo número: "))
                self.num3 = float(input("Digite o terceiro número: "))
                break
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    def encontrar_maior_numero(self):
        return max(self.num1, self.num2, self.num3)


def main():
    maior_num = MaiorNumero()
    maior_num.obter_numeros()

    maior = maior_num.encontrar_maior_numero()

    print(f"O maior número é: {maior}")


if __name__ == '__main__':
    main()
