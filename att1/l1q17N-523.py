#Lista de Exercício 1 - Questão 17
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import math

class LojaTintas:
    def __init__(self, area):
        self.area = area

    def calcular_quantidade_latas(self):
        litros_tinta = self.area / 6
        latas = math.ceil(litros_tinta / 18)
        return latas

    def calcular_preco_latas(self, latas):
        preco_lata = 80.00
        preco_total = latas * preco_lata
        return preco_total

    def calcular_quantidade_galoes(self):
        litros_tinta = self.area / 6
        galoes = math.ceil(litros_tinta / 3.6)
        return galoes

    def calcular_preco_galoes(self, galoes):
        preco_galao = 25.00
        preco_total = galoes * preco_galao
        return preco_total

    def calcular_mistura_latas_galoes(self):
        litros_tinta = self.area / 6
        latas = math.floor(litros_tinta / 18)
        litros_restantes = litros_tinta - latas * 18
        galoes = math.ceil(litros_restantes / 3.6)

        preco_latas = latas * 80.00
        preco_galoes = galoes * 25.00
        preco_total = preco_latas + preco_galoes
        return (latas, galoes, preco_total)


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
    preco_latas = loja_tintas.calcular_preco_latas(latas)

    galoes = loja_tintas.calcular_quantidade_galoes()
    preco_galoes = loja_tintas.calcular_preco_galoes(galoes)

    mistura_latas_galoes = loja_tintas.calcular_mistura_latas_galoes()
    latas_mistura, galoes_mistura, preco_mistura = mistura_latas_galoes

    print(f"Situação 1: Comprar apenas latas de 18 litros")
    print(f"Quantidade de latas: {latas}")
    print(f"Preço total: R$ {preco_latas:.2f}\n")

    print(f"Situação 2: Comprar apenas galões de 3,6 litros")
    print(f"Quantidade de galões: {galoes}")
    print(f"Preço total: R$ {preco_galoes:.2f}\n")

    print(f"Situação 3: Misturar latas e galões")
    print(f"Quantidade de latas: {latas_mistura}")
    print(f"Quantidade de galões: {galoes_mistura}")
    print(f"Preço total: R$ {preco_mistura:.2f}")


if __name__ == '__main__':
    main()
