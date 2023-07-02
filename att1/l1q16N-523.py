#Lista de Exercício 1 - Questão 16
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class LojaTintas:
    def __init__(self, area):
        self.area = area

    def calcular_quantidade_latas(self):
        litros_tinta = self.area / 3
        latas = math.ceil(litros_tinta / 18)
        return latas

    def calcular_preco_total(self, latas):
        preco_lata = 80.00
        preco_total = latas * preco_lata
        return preco_total


def obter_valor_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")


def main():
    area = obter_valor_numerico("Informe o tamanho da área a ser pintada em metros quadrados: ")

    loja_tintas = LojaTintas(area)

    latas = loja_tintas.calcular_quantidade_latas()
    preco_total = loja_tintas.calcular_preco_total(latas)

    print(f"Quantidade de latas de tinta: {latas}")
    print(f"Preço total: R$ {preco_total:.2f}")


if __name__ == '__main__':
    main()
