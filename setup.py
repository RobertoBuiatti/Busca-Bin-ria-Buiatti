from setuptools import setup, find_packages

setup(
    name="buscabinaria-buiatti",
    version="0.1.0",
    author="Roberto Caetano Buiatti",
    description="Implementação otimizada do algoritmo de busca binária com verificações laterais",
    long_description="""
    Uma implementação otimizada do algoritmo de busca binária que verifica os elementos 
    adjacentes ao meio a cada iteração, aumentando a eficiência da busca sem 
    comprometer a complexidade do algoritmo.
    
    Características:
    - Verificação rápida de limites
    - Verificação otimizada de elementos adjacentes
    - Suporte a diferentes tipos de sequências (listas, tuplas)
    - Tipagem estática com suporte a genéricos
    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.7",
    install_requires=[],
    keywords="busca binária, algoritmos, otimização, estruturas de dados",
)
