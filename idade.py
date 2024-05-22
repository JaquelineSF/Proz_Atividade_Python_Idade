import datetime

def calcular_idade(ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        ano_nascimento = input("Digite o ano de nascimento (entre 1922 e 2021): ")
        if ano_nascimento.isdigit():
            ano_nascimento = int(ano_nascimento)
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Erro: O ano de nascimento deve estar entre 1922 e 2021.")
        else:
            print("Erro: Por favor, digite um ano válido.")

def main():
    nome_completo = input("Digite o seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    
    idade = calcular_idade(ano_nascimento)
    
    print("\nNome:", nome_completo)
    print("Idade em 2022:", idade)

if __name__ == "__main__":
    main()
