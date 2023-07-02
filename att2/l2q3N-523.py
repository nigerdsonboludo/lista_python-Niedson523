#Lista de Exercício 2 - Questão 3
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class VerificadorSexo:
    def __init__(self, letra):
        self.letra = letra

    def verificar_sexo(self):
        if self.letra.upper() == "F":
            return "Feminino"
        elif self.letra.upper() == "M":
            return "Masculino"
        else:
            return "Sexo Inválido"


def obter_letra(mensagem):
    while True:
        letra = input(mensagem)
        if letra.upper() == "F" or letra.upper() == "M":
            return letra.upper()
        else:
            print("Letra inválida. Digite 'F' para Feminino ou 'M' para Masculino.")


def main():
    letra = obter_letra("Digite uma letra (F ou M): ")

    verificador = VerificadorSexo(letra)
    resultado = verificador.verificar_sexo()

    print(f"O sexo é {resultado}.")


if __name__ == '__main__':
    main()
