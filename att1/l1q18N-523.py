#Lista de Exercício 1 - Questão 18
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def calcular_tempo_download(tamanho_arquivo, velocidade_internet):
    tamanho_bits = tamanho_arquivo * 8 * 1024 * 1024
    tempo_segundos = tamanho_bits / (velocidade_internet * 1024 * 1024)
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

def main():
    tamanho_arquivo = float(input("Informe o tamanho do arquivo em MB: "))
    velocidade_internet = float(input("Informe a velocidade do link de Internet em Mbps: "))

    tempo_download = calcular_tempo_download(tamanho_arquivo, velocidade_internet)

    print(f"O tempo aproximado de download do arquivo é de {tempo_download:.2f} minutos.")

if __name__ == '__main__':
    main()
