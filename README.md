# Busca Binária Buiatti

A **Busca Binária Buiatti** é uma biblioteca em Python que implementa o algoritmo de busca binária personalizado, permitindo localizar a posição de um elemento específico em uma lista ordenada de maneira eficiente que o da busca binária tradicional.

## Descrição

A busca binária é um algoritmo de pesquisa que encontra a posição de um valor em uma lista ordenada, dividindo repetidamente o espaço de busca pela metade até localizar o elemento desejado. Este método é mais eficiente que a busca linear, especialmente para listas grandes, pois reduz o número de comparações necessárias.

## Requisitos

* Python 3.x

## Instalação

Para instalar a biblioteca, clone este repositório em seu ambiente local:

<pre class="!overflow-visible" data-start="684" data-end="765"><span>git clone https://github.com/RobertoBuiatti/Busca-Binaria-Buiatti.git
</span></code></div></div></pre>

Em seguida, navegue até o diretório do projeto:

<pre class="!overflow-visible" data-start="818" data-end="854"><span>cd Busca-Binaria-Buiatti
</span></code></div></div></pre>

E instale a biblioteca utilizando o `setup.py`:

<pre class="!overflow-visible" data-start="907" data-end="942"><span>python setup.py install
</span></code></div></div></pre>

## Uso

Após a instalação, você pode utilizar a função de busca binária em seu código Python da seguinte forma:

<pre class="!overflow-visible" data-start="1059" data-end="1424"><span>from buscabinaria_buiatti import busca_binaria

# Lista ordenada de exemplo
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Elemento a ser buscado
elemento = 7

# Realiza a busca binária
indice = busca_binaria(lista, elemento)

if indice != -1:
    print(f"Elemento encontrado na posição: {indice}")
else:
    print("Elemento não encontrado na lista.")
</span></code></div></div></pre>
<<<<<<< HEAD


=======
>>>>>>> 7a3c405 (alteração readme)
