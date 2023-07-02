#Lista de Exercício 2 - Questão 19
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class DecomporNumero:
    def __init__(self):
        self.numero = 0

    def ler_numero(self):
        while True:
            try:
                self.numero = int(input("Digite um número inteiro menor que 1000: "))
                if self.numero >= 0 and self.numero < 1000:
                    break
                else:
                    print("Número inválido. Digite um número inteiro menor que 1000.")
            except ValueError:
                print("Número inválido. Digite um número inteiro válido.")

    def decompor(self):
        centenas = self.numero // 100
        dezenas = (self.numero % 100) // 10
        unidades = (self.numero % 100) % 10

        return centenas, dezenas, unidades

    def exibir_resultado(self):
        centenas, dezenas, unidades = self.decompor()

        resultado = ""
        if centenas > 0:
            resultado += "{} centena(s), ".format(centenas)
        if dezenas > 0:
            resultado += "{} dezena(s), ".format(dezenas)
        if unidades > 0 or self.numero == 0:
            resultado += "{} unidade(s)".format(unidades)

        print(resultado)


def main():
    numero = DecomporNumero()
    numero.ler_numero()
    numero.exibir_resultado()


if __name__ == "__main__":
    main()
