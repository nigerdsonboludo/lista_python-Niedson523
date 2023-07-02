#Lista de Exercício 2 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class VerificadorLetra:
    def __init__(self, letra):
        self.letra = letra

    def verificar_tipo_letra(self):
        if self.letra.upper() in ['A', 'E', 'I', 'O', 'U']:
            return "Vogal"
        else:
            return "Consoante"


def obter_letra(mensagem):
    while True:
        try:
            letra = input(mensagem)
            if len(letra) == 1 and letra.isalpha():
                return letra.upper()
            else:
                raise ValueError
        except ValueError:
            print("Entrada inválida. Digite apenas uma única letra.")


def main():
    letra = obter_letra("Digite uma letra: ")

    verificador = VerificadorLetra(letra)
    resultado = verificador.verificar_tipo_letra()

    print(f"A letra digitada é {resultado}.")


if __name__ == '__main__':
    main()
