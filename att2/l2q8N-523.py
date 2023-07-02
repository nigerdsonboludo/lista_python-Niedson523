#Lista de Exercício 2 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Compra:
    def __init__(self, preco1, preco2, preco3):
        self.preco1 = preco1
        self.preco2 = preco2
        self.preco3 = preco3

    def encontrar_mais_barato(self):
        mais_barato = min(self.preco1, self.preco2, self.preco3)
        if mais_barato == self.preco1:
            return "Produto 1"
        elif mais_barato == self.preco2:
            return "Produto 2"
        else:
            return "Produto 3"

try:
    preco1 = float(input("Digite o preço do Produto 1: "))
    preco2 = float(input("Digite o preço do Produto 2: "))
    preco3 = float(input("Digite o preço do Produto 3: "))

    compra = Compra(preco1, preco2, preco3)
    produto_mais_barato = compra.encontrar_mais_barato()

    print("Você deve comprar:", produto_mais_barato)

except ValueError:
    print("Erro: digite apenas números.")
