#Lista de Exercício 2 - Questão 2
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def verificar_positivo_negativo(valor):
    if valor > 0:
        return "positivo"
    elif valor < 0:
        return "negativo"
    else:
        return "zero"


def obter_valor_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")


def main():
    valor = obter_valor_numerico("Digite um valor: ")

    resultado = verificar_positivo_negativo(valor)

    print(f"O valor é {resultado}.")


if __name__ == '__main__':
    main()
