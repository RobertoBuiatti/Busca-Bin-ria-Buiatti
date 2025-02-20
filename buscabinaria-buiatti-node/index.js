/**
 * Implementação otimizada de busca binária com verificações laterais.
 * 
 * @template T
 * @param {Array<T>} array - Array ordenado de elementos
 * @param {T} alvo - Elemento a ser procurado
 * @returns {number} - Índice do elemento encontrado ou -1 se não encontrado
 * 
 * @example
 * const lista = [1, 3, 5, 7, 9];
 * const indice = buscaBinariaBuiatti(lista, 5); // Retorna: 2
 */
function buscaBinariaBuiatti(array, alvo) {
    // Verifica se o array está vazio
    const tamanho = array.length;
    if (tamanho === 0) {
        return -1;
    }

    // Verificação rápida de limites
    if (alvo < array[0] || alvo > array[tamanho - 1]) {
        return -1;
    }

    // Verificação das bordas
    if (array[0] === alvo) {
        return 0;
    }
    if (array[tamanho - 1] === alvo) {
        return tamanho - 1;
    }

    // Inicializa os ponteiros ignorando as bordas já verificadas
    let esquerda = 1;
    let direita = tamanho - 2;

    while (esquerda <= direita) {
        // Divisão por 2 utilizando shift bit a bit (mais eficiente)
        const meio = (esquerda + direita) >> 1;
        const valorMeio = array[meio];

        // Verifica o elemento central
        if (valorMeio === alvo) {
            return meio;
        }

        // Verifica o vizinho à esquerda, se estiver dentro dos limites atuais
        if (meio - 1 >= esquerda && array[meio - 1] === alvo) {
            return meio - 1;
        }

        // Verifica o vizinho à direita, se estiver dentro dos limites atuais
        if (meio + 1 <= direita && array[meio + 1] === alvo) {
            return meio + 1;
        }

        // Atualiza os ponteiros, pulando os elementos já verificados
        if (valorMeio < alvo) {
            esquerda = meio + 2; // pula o vizinho à direita já verificado
        } else {
            direita = meio - 2; // pula o vizinho à esquerda já verificado
        }
    }

    return -1;
}

module.exports = buscaBinariaBuiatti;
