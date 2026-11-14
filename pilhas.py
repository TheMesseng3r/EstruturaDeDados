# Trabalho 01 - Estrutura de Dados;
# Implementação do tipo abstrato de dados Pilha(estática);
# Prof. Dr. Franklin César Flores
# Alunos: Lucas Santana Zanzim RA: 143393
#         Gabriel Lopes Pinel de Carvalho RA: 152703;

# Definição do tipo Pilha com class, possui elem, um vetor onde os elementos da pilha serão armazenados, e topo,
# posição do último elemento da pilha;
# TamMax é uma constante que define o tamanho físico do vetor (armazena, no máximo, TamMax + 1 elementos);
class Pilha:
    elem: list
    TamMax: int
    topo: int

    def __init__(self):
        self.TamMax = 99
        self.elem = [0] * (self.TamMax + 1)
        self.topo = -1


# Esvazia a pilha declarada, onde o topo da pilha receberá o valor -1, ou seja, não possui nenhum elemento armazenado;
def inicializa_pilha(P: Pilha) -> None:
    P.topo = -1


# Verifica se a pilha está vazia ou não, retornando True ou False;
def pilha_vazia(P: Pilha) -> bool:
    return P.topo == -1


# Verifica se a pilha está cheia ou não, retornando True ou False;
def pilha_cheia(P: Pilha) -> bool:
    return P.topo == P.TamMax


# Coloca um novo valor no topo da Pilha;
# Retorna True se o elemento foi empilhado;
def empilha(P: Pilha, x: int):
    if not pilha_cheia(P):
        P.topo = P.topo + 1
        P.elem[P.topo] = x
        return True


# Retira um valor do topo da Pilha e o devolve;
def desempilha(P: Pilha):
    if not pilha_vazia(P):
        x = P.elem[P.topo]
        P.topo = P.topo - 1
        return x


# Retorna o valor que está no topo da Pilha, sem removê-lo;
# Retorna erro se a pilha estiver vazia;
def elemento_do_topo(P: Pilha):
    if not pilha_vazia(P):
        return P.elem[P.topo]
    else:
        print("Erro: pilha vazia")
