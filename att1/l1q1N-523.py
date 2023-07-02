#Lista de Exercício 1 - Questão 1
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#1. Faça um Programa que mostre a mensagem "Alo mundo" na tela. 

class Mensagem:
    def __init__(self, texto):
        self.texto = texto
    def mostrar(self):
        print(self.texto)

def main():
    try:
        mensagem = Mensagem("Alô mundo")
        mensagem.mostrar()
    except Exception as erro:
        print("Ocorreu um erro:", erro)

if __name__ == "__main__":
    main()