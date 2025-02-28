Busca Binária Buiatti
A Busca Binária Buiatti é uma biblioteca em Node.js que implementa o algoritmo de busca binária personalizado, permitindo localizar a posição de um elemento específico em uma lista ordenada de maneira mais eficiente que a busca binária tradicional.

Descrição
A busca binária é um algoritmo de pesquisa que encontra a posição de um valor em uma lista ordenada, dividindo repetidamente o espaço de busca pela metade até localizar o elemento desejado. Este método é mais eficiente que a busca linear, especialmente para listas grandes, pois reduz o número de comparações necessárias.

Requisitos
Node.js (versão recomendada 14.x ou superior)
Instalação
Para instalar a biblioteca, você pode clonar este repositório em seu ambiente local:

<pre class="!overflow-visible">

git clone https://github.com/RobertoBuiatti/Busca-Binaria-Buiatti.git

</pre>

Em seguida, navegue até o diretório do projeto Node:

<pre class="!overflow-visible">

cd Busca-Binaria-Buiatti/buscabinaria-buiatti-node

</pre>

E instale as dependências:

<pre class="!overflow-visible">

npm install

</pre>

Uso
Após a instalação, você pode utilizar a função de busca binária em seu código JavaScript da seguinte forma:

<pre class="!overflow-visible">

const { buscaBinaria } = require('buscabinaria-buiatti');

// Lista ordenada de exemplo

const lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];

// Elemento a ser buscado

const elemento = 7;

// Realiza a busca binária

const indice = buscaBinaria(lista, elemento);

if (indice !== -1) {

console.log(`Elemento encontrado na posição: ${indice}`);

} else {

console.log("Elemento não encontrado na lista.");

}

</pre>

Observações de Uso
Lista Ordenada: A biblioteca exige que a lista fornecida esteja ordenada em ordem crescente para funcionar corretamente.

Tipos de Dados: A busca binária funciona com arrays de números, strings e objetos, desde que haja uma ordem definida entre os elementos.
Tempo de Execução: O algoritmo tem complexidade de tempo O(log n), tornando-o muito eficiente para grandes conjuntos de dados.

Retorno da Função:
Retorna o índice (posição) do elemento na lista quando encontrado
Retorna -1 quando o elemento não está presente na lista

Elementos Duplicados: Se a lista contiver elementos duplicados, a função retornará o índice da primeira ocorrência encontrada.

Performance: Para listas muito pequenas (menos de 10 elementos), uma busca linear pode ser mais eficiente devido à menor sobrecarga.

Compatibilidade: A biblioteca é compatível com todas as versões recentes do Node.js e pode ser utilizada em projetos front-end através de bundlers como Webpack ou Browserify.
