"""
Implementação otimizada do algoritmo de busca binária com verificações laterais.
"""
from typing import Sequence, TypeVar, Optional

T = TypeVar('T')

def busca_binaria_buiatti(sequencia: Sequence[T], alvo: T) -> int:
    """
    Implementação otimizada de busca binária com verificações laterais.
    
    Esta implementação verifica os elementos imediatamente à esquerda e à direita 
    do meio a cada iteração, aumentando a chance de encontrar o alvo sem aumentar 
    a complexidade.

    Args:
        sequencia: Uma sequência ordenada de elementos (lista, tupla, etc.)
        alvo: O valor a ser procurado na sequência

    Returns:
        int: O índice do elemento encontrado, ou -1 se não encontrado

    Exemplo:
        >>> lista = [1, 3, 5, 7, 9, 11, 13]
        >>> busca_binaria_buiatti(lista, 7)
        3
        >>> busca_binaria_buiatti(lista, 4)
        -1
    """
    tamanho = len(sequencia)
    if tamanho == 0:
        return -1

    # Verificação rápida de limites
    if alvo < sequencia[0] or alvo > sequencia[-1]:
        return -1

    # Verificação das bordas
    if sequencia[0] == alvo:
        return 0
    if sequencia[-1] == alvo:
        return tamanho - 1

    # Inicializa os ponteiros ignorando as bordas já verificadas
    esquerda, direita = 1, tamanho - 2

    while esquerda <= direita:
        meio = (esquerda + direita) >> 1  # Divisão por 2 utilizando shift bit a bit
        valor_meio = sequencia[meio]

        # Verifica o elemento central
        if valor_meio == alvo:
            return meio

        # Verifica o vizinho à esquerda, se estiver dentro dos limites atuais
        if meio - 1 >= esquerda and sequencia[meio - 1] == alvo:
            return meio - 1

        # Verifica o vizinho à direita, se estiver dentro dos limites atuais
        if meio + 1 <= direita and sequencia[meio + 1] == alvo:
            return meio + 1

        # Atualiza os ponteiros, pulando os elementos já verificados
        if valor_meio < alvo:
            esquerda = meio + 2  # pula o vizinho à direita já verificado
        else:
            direita = meio - 2  # pula o vizinho à esquerda já verificado

    return -1

def _executar_testes():
    """Executa testes básicos do algoritmo."""
    # Teste 1: Lista vazia
    assert busca_binaria_buiatti([], 1) == -1, "Falha no teste com lista vazia"

    # Teste 2: Lista com um elemento
    assert busca_binaria_buiatti([1], 1) == 0, "Falha no teste com lista de um elemento"
    assert busca_binaria_buiatti([1], 2) == -1, "Falha no teste com elemento não encontrado"

    # Teste 3: Lista com múltiplos elementos
    lista = [1, 3, 5, 7, 9, 11, 13, 15]
    assert busca_binaria_buiatti(lista, 1) == 0, "Falha na busca do primeiro elemento"
    assert busca_binaria_buiatti(lista, 15) == 7, "Falha na busca do último elemento"
    assert busca_binaria_buiatti(lista, 7) == 3, "Falha na busca do elemento do meio"
    assert busca_binaria_buiatti(lista, 4) == -1, "Falha na busca de elemento inexistente"

    # Teste 4: Tupla como entrada
    tupla = tuple(range(0, 20, 2))  # (0, 2, 4, ..., 18)
    assert busca_binaria_buiatti(tupla, 10) == 5, "Falha na busca em tupla"
    assert busca_binaria_buiatti(tupla, 11) == -1, "Falha na busca de elemento inexistente em tupla"

    print("Todos os testes passaram com sucesso!")

if __name__ == '__main__':
    _executar_testes()
