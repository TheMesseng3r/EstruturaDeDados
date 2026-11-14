# Trabalho 02 - Estrutura de Dados;
# Avaliação de expressões em notação posfixa utilizando o tipo abstrato de dados Pilha (estática);
# Prof. Dr. Franklin César Flores
# Alunos: Lucas Santana Zanzim RA: 143393
#         Gabriel Lopes Pinel de Carvalho RA: 152703;

# Importa as funções de pilhas para fazer as contas da expressões;
from pilhas import Pilha, inicializa_pilha, pilha_vazia, empilha, desempilha


# Divisão inteira com resultado apenas da parte inteira
# Descobre se o resultado deve ser negativo, divide os valores absolutos
# e Reaplica o sinal;
def divide(a: int, b: int) -> int:
    negativo = (a < 0) != (b < 0)
    
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    q = a // b
    if negativo:
        q = -q
        
    return q


# Avalia a expressão posfixa. Retorna True, resultado, ou False, mensagem de erro;
def avalia(expressao: str):
    # Cria a pilha e duas variáveis auxiliares;
    P = Pilha()
    inicializa_pilha(P)
    numero = 0
    lendo_numero = False

# Dentro do laço será feito todo o cálculo da expressão por completo;
    for c in expressao:
        # Converte os caracteres nos valores respectivos;
        # Multiplicar o valor por 10 desloca o que já foi lido uma casa para a esquerda;
        if "0" <= c <= "9":
            numero = numero * 10 + (ord(c) - ord("0"))
            lendo_numero = True
        
        # Ponto marca o fim do operando, o número pronto é empilhado e as variáveis voltam
        # ao estado inicial;
        elif c == ".":
            # Evita empilhar um zero falso se aparecer um ponto sem um número antes dele
            # empilha devolve False se a pilha estiver cheia, e nesse caso o laço para com um erro;
            if lendo_numero:
                if not empilha(P, numero):
                    return False, "Erro: pilha cheia"
            numero = 0
            lendo_numero = False
            
        # Um operador precisa de dois operandos, se a pilha estiver vazia em qualquer uma
        # das retiradas, falta operando e a função encerra com erro;
        elif c in "+-*/":
            if pilha_vazia(P):
                return False, "Erro: faltando operando"
            b = desempilha(P)
            
            if pilha_vazia(P):
                return False, "Erro: faltando operando"
            a = desempilha(P)

            # Cálculo dos valores;
            if c == "+":
                r = a + b
            elif c == "-":
                r = a - b
            elif c == "*":
                r = a * b
            else:
                if b == 0:
                    return False, "Erro: divisão por zero"
                r = divide(a, b)
            empilha(P, r)

    # Verificação final
    # Se a pilha acabou vazia, então faltou operando;
    if pilha_vazia(P):
        return False, "Erro: faltando operando"
    resultado = desempilha(P)
    # Se depois de retirar o resultado, ainda sobrou algo, então faltou operador;
    if not pilha_vazia(P):
        return False, "Erro: faltando operador"
    return True, resultado


def main():
# Pede o arquivo de teste;
    nome = input("Digite o nome do arquivo: ").strip()
    try:
        arquivo = open(nome, "r")
    except OSError:
        print("Não foi possível abrir o arquivo:", nome)
        return

# Separa as expressões linha por linha e fornece o resultado das expressões;
    n = 0
    for linha in arquivo:
        linha = linha.strip()
        if linha == "":
            continue
        n = n + 1
        saida = avalia(linha)[1]
        print("Expressão", n, ":", saida)
    arquivo.close()


if __name__ == "__main__":
    main()
