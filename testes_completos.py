"""
Testes completos para a biblioteca BuscaBinariaBuiatti
"""
import random
from typing import List, Any, Tuple
from buscabinaria_buiatti import busca_binaria_buiatti

def gerar_lista_teste(tamanho: int, ordenada: bool = True) -> Tuple[List[int], List[int]]:
    """Gera uma lista de teste e seus alvos"""
    lista = list(range(tamanho))
    if not ordenada:
        random.shuffle(lista)
    alvos = lista[::2]  # Pega metade dos números como alvos
    alvos.extend([max(lista) + 1, min(lista) - 1])  # Adiciona valores fora da lista
    return lista, alvos

def testar_tipos_diferentes():
    """Testa a busca com diferentes tipos de dados"""
    print("\nTestando diferentes tipos de dados:")
    
    # Teste com strings
    lista_str = ['a', 'b', 'c', 'd', 'e']
    assert busca_binaria_buiatti(lista_str, 'c') == 2
    assert busca_binaria_buiatti(lista_str, 'f') == -1
    print("✓ Teste com strings passou")
    
    # Teste com floats
    lista_float = [1.1, 2.2, 3.3, 4.4, 5.5]
    assert busca_binaria_buiatti(lista_float, 3.3) == 2
    assert busca_binaria_buiatti(lista_float, 6.6) == -1
    print("✓ Teste com floats passou")
    
    # Teste com tuplas
    lista_tupla = tuple([1, 2, 3, 4, 5])
    assert busca_binaria_buiatti(lista_tupla, 3) == 2
    print("✓ Teste com tuplas passou")

def testar_casos_especiais():
    """Testa casos especiais e limites"""
    print("\nTestando casos especiais:")
    
    # Lista vazia
    assert busca_binaria_buiatti([], 1) == -1
    print("✓ Lista vazia")
    
    # Lista com um elemento
    assert busca_binaria_buiatti([1], 1) == 0
    assert busca_binaria_buiatti([1], 2) == -1
    print("✓ Lista com um elemento")
    
    # Lista com elementos duplicados
    lista_dup = [1, 2, 2, 2, 3]
    indice = busca_binaria_buiatti(lista_dup, 2)
    assert lista_dup[indice] == 2
    print("✓ Lista com elementos duplicados")
    
    # Valores nos limites
    lista = [1, 2, 3, 4, 5]
    assert busca_binaria_buiatti(lista, 1) == 0  # Primeiro elemento
    assert busca_binaria_buiatti(lista, 5) == 4  # Último elemento
    assert busca_binaria_buiatti(lista, 0) == -1  # Menor que o menor
    assert busca_binaria_buiatti(lista, 6) == -1  # Maior que o maior
    print("✓ Valores nos limites")

def testar_desempenho():
    """Testa o desempenho com listas grandes"""
    print("\nTestando desempenho:")
    
    # Teste com lista grande
    tamanho = 1000000
    lista, alvos = gerar_lista_teste(tamanho)
    
    # Testa alguns valores aleatórios
    for alvo in random.sample(alvos, 10):
        resultado = busca_binaria_buiatti(lista, alvo)
        if alvo in lista:
            assert resultado != -1 and lista[resultado] == alvo
        else:
            assert resultado == -1
    
    print(f"✓ Teste com lista de {tamanho:,} elementos passou")

def executar_todos_testes():
    """Executa todos os testes"""
    print("=== Iniciando testes completos da biblioteca BuscaBinariaBuiatti ===")
    
    try:
        testar_tipos_diferentes()
        testar_casos_especiais()
        testar_desempenho()
        
        print("\n✅ Todos os testes passaram com sucesso!")
        return True
    except AssertionError as e:
        print(f"\n❌ Falha nos testes: {str(e)}")
        return False
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")
        return False

if __name__ == '__main__':
    executar_todos_testes()
