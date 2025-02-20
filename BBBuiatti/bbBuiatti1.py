# Importações básicas
import os
import time
import random
import psutil
import tracemalloc
from typing import Dict, List, Tuple, Optional
import warnings
from functools import lru_cache
from concurrent.futures import ProcessPoolExecutor

# Importações para análise de dados e estatísticas
import numpy as np
import pandas as pd
from scipy import stats

# Importações para visualização
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração para suprimir avisos
warnings.filterwarnings("ignore")
plt.style.use("default")

# Criar diretório para resultados
os.makedirs("resultados", exist_ok=True)


class BuscaBinariaAnalise:
    def __init__(self):
        self.cache_hits = 0
        self.cache_misses = 0

    @staticmethod
    def calcular_melhoria_percentual(
        tempo_original: float, tempo_modificada: float
    ) -> float:
        """
        Calcula a melhoria percentual entre os tempos de execução.
        """
        if tempo_original == 0 or tempo_modificada == 0:
            return 0.0
        return ((tempo_original - tempo_modificada) / tempo_original) * 100

    def plotar_comparativo_tempos(self, dados_por_caso: Dict) -> None:
        """
        Gera gráficos comparativos de tempo para cada caso de teste.
        """
        # Garantir que o diretório existe
        os.makedirs("resultados", exist_ok=True)

        for caso, dados in dados_por_caso.items():
            plt.figure(figsize=(12, 6))

            # Extrair dados
            tamanhos = dados["Tamanho da Lista"]
            tempos_orig = [
                d["metricas_original"]["tempo_execucao"] for d in dados["metricas"]
            ]
            tempos_mod = [
                d["metricas_modificada"]["tempo_execucao"] for d in dados["metricas"]
            ]

            # Plotar tempos
            plt.plot(tamanhos, tempos_orig, marker="o", color="blue", label="Original")
            plt.plot(tamanhos, tempos_mod, marker="s", color="red", label="Modificada")

            plt.xscale("log")
            plt.yscale("log")
            plt.title(f"Comparação dos Tempos de Execução - {caso}")
            plt.xlabel("Tamanho da Lista (escala log)")
            plt.ylabel("Tempo (s) (escala log)")
            plt.grid(True, alpha=0.3)
            plt.legend()

            # Adicionar anotações de melhoria
            media_melhoria = np.mean(
                [
                    self.calcular_melhoria_percentual(orig, mod)
                    for orig, mod in zip(tempos_orig, tempos_mod)
                ]
            )
            plt.annotate(
                f"Melhoria Média: {media_melhoria:.2f}%",
                xy=(0.02, 0.95),
                xycoords="axes fraction",
                bbox=dict(facecolor="white", alpha=0.8),
            )

            plt.tight_layout()
            nome_arquivo = (
                caso.lower().replace(" ", "_").replace("í", "i").replace("ê", "e")
            )
            plt.savefig(
                f"resultados/comparativo_tempos_{nome_arquivo}.png",
                dpi=300,
                bbox_inches="tight",
            )
            plt.close()

    def plotar_melhorias_percentuais(self, dados_por_caso: Dict) -> None:
        """
        Gera gráficos de melhoria percentual para cada caso de teste.
        """
        # Garantir que o diretório existe
        os.makedirs("resultados", exist_ok=True)

        plt.figure(figsize=(15, 8))
        medias_melhorias = []
        casos = []

        for caso, dados in dados_por_caso.items():
            tempos_orig = [
                d["metricas_original"]["tempo_execucao"] for d in dados["metricas"]
            ]
            tempos_mod = [
                d["metricas_modificada"]["tempo_execucao"] for d in dados["metricas"]
            ]

            melhorias = [
                self.calcular_melhoria_percentual(orig, mod)
                for orig, mod in zip(tempos_orig, tempos_mod)
            ]

            medias_melhorias.append(np.mean(melhorias))
            casos.append(caso)

        # Criar gráfico de barras
        plt.figure(figsize=(15, 8))
        bars = plt.bar(casos, medias_melhorias)
        plt.xticks(rotation=45, ha="right")
        plt.title("Média de Melhoria Percentual por Caso de Teste")
        plt.ylabel("Melhoria Percentual (%)")
        plt.grid(True, axis="y", alpha=0.3)

        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f"{height:.1f}%",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        plt.savefig(
            "resultados/melhorias_percentuais.png", dpi=300, bbox_inches="tight"
        )
        plt.close()

    def plotar_distribuicao_melhorias(self, dados_por_caso: Dict) -> None:
        """
        Gera gráfico de violino mostrando a distribuição das melhorias.
        """
        # Garantir que o diretório existe
        os.makedirs("resultados", exist_ok=True)

        melhorias_por_caso = []
        casos = []

        for caso, dados in dados_por_caso.items():
            tempos_orig = [
                d["metricas_original"]["tempo_execucao"] for d in dados["metricas"]
            ]
            tempos_mod = [
                d["metricas_modificada"]["tempo_execucao"] for d in dados["metricas"]
            ]

            melhorias = [
                self.calcular_melhoria_percentual(orig, mod)
                for orig, mod in zip(tempos_orig, tempos_mod)
            ]

            melhorias_por_caso.extend(melhorias)
            casos.extend([caso] * len(melhorias))

        df = pd.DataFrame({"Caso": casos, "Melhoria (%)": melhorias_por_caso})

        plt.figure(figsize=(15, 8))
        sns.violinplot(x="Caso", y="Melhoria (%)", data=df)
        plt.xticks(rotation=45, ha="right")
        plt.title("Distribuição das Melhorias por Caso de Teste")
        plt.grid(True, axis="y", alpha=0.3)
        plt.tight_layout()
        plt.savefig(
            "resultados/distribuicao_melhorias.png", dpi=300, bbox_inches="tight"
        )
        plt.close()

    def plotar_analises_detalhadas(self, dados_por_caso: Dict) -> None:
        """
        Gera múltiplas visualizações detalhadas dos resultados.
        """
        # Garantir que o diretório existe
        os.makedirs("resultados", exist_ok=True)

        # Plotar comparativos individuais por caso
        self.plotar_comparativo_tempos(dados_por_caso)

        # Plotar melhorias percentuais
        self.plotar_melhorias_percentuais(dados_por_caso)

        # Plotar distribuição de melhorias
        self.plotar_distribuicao_melhorias(dados_por_caso)

    @staticmethod
    def medir_recursos(func):
        """
        Decorator para medir recursos computacionais de uma função.
        """

        def wrapper(*args, **kwargs):
            tracemalloc.start()
            processo = psutil.Process(os.getpid())
            cpu_inicio = processo.cpu_percent()
            memoria_inicio = processo.memory_info().rss
            tempo_inicio = time.perf_counter()

            resultado = func(*args, **kwargs)

            tempo_final = time.perf_counter()
            cpu_final = processo.cpu_percent()
            memoria_final = processo.memory_info().rss
            _, pico_memoria = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            metricas = {
                "tempo_execucao": tempo_final - tempo_inicio,
                "uso_cpu": (cpu_final + cpu_inicio) / 2,
                "uso_memoria": memoria_final - memoria_inicio,
                "pico_memoria": pico_memoria,
            }

            return resultado, metricas

        return wrapper

    @staticmethod
    @lru_cache(maxsize=1024)
    def busca_binaria_original(lista_tuple: tuple, alvo: int) -> int:
        """
        Implementação original da busca binária com cache.
        """
        lista = list(lista_tuple)
        esquerda = 0
        direita = len(lista) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if lista[meio] == alvo:
                return meio
            elif lista[meio] < alvo:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1

    @staticmethod
    def busca_binaria_buiatti(lista_tuple: tuple, alvo: int) -> int:
        """
        Implementação otimizada de busca binária com verificações laterais.
        Verifica os elementos imediatamente à esquerda e à direita do meio a cada iteração,
        aumentando a chance de encontrar o alvo sem aumentar a complexidade.
        """
        tamanho = len(lista_tuple)
        if tamanho == 0:
            return -1

        # Verificação rápida de limites
        if alvo < lista_tuple[0] or alvo > lista_tuple[-1]:
            return -1

        # Verificação das bordas
        if lista_tuple[0] == alvo:
            return 0
        if lista_tuple[-1] == alvo:
            return tamanho - 1

        # Inicializa os ponteiros ignorando as bordas já verificadas
        esquerda, direita = 1, tamanho - 2

        while esquerda <= direita:
            meio = (esquerda + direita) >> 1  # Divisão por 2 utilizando shift bit a bit
            valor_meio = lista_tuple[meio]

            # Verifica o elemento central
            if valor_meio == alvo:
                return meio

            # Verifica o vizinho à esquerda, se estiver dentro dos limites atuais
            if meio - 1 >= esquerda and lista_tuple[meio - 1] == alvo:
                return meio - 1

            # Verifica o vizinho à direita, se estiver dentro dos limites atuais
            if meio + 1 <= direita and lista_tuple[meio + 1] == alvo:
                return meio + 1

            # Atualiza os ponteiros, pulando os elementos já verificados
            if valor_meio < alvo:
                esquerda = meio + 2  # pula o vizinho à direita já verificado
            else:
                direita = meio - 2  # pula o vizinho à esquerda já verificado

        return -1

    @staticmethod
    def executar_teste_paralelo(args: Tuple) -> Dict:
        """
        Executa um teste individual para paralelização com medição de recursos.
        """
        lista, alvo, tamanho_lista = args

        # Medir busca original
        inicio_original = time.perf_counter()
        tracemalloc.start()
        processo = psutil.Process(os.getpid())
        cpu_inicio = processo.cpu_percent()
        memoria_inicio = processo.memory_info().rss

        resultado_original = BuscaBinariaAnalise.busca_binaria_original(
            tuple(lista), alvo
        )

        tempo_original = time.perf_counter() - inicio_original
        cpu_final = processo.cpu_percent()
        memoria_final = processo.memory_info().rss
        _, pico_memoria_original = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        metricas_original = {
            "tempo_execucao": tempo_original,
            "uso_cpu": (cpu_final + cpu_inicio) / 2,
            "uso_memoria": memoria_final - memoria_inicio,
            "pico_memoria": pico_memoria_original,
        }

        # Medir busca modificada
        inicio_modificada = time.perf_counter()
        tracemalloc.start()
        cpu_inicio = processo.cpu_percent()
        memoria_inicio = processo.memory_info().rss

        resultado_modificada = BuscaBinariaAnalise.busca_binaria_buiatti(
            tuple(lista), alvo
        )

        tempo_modificada = time.perf_counter() - inicio_modificada
        cpu_final = processo.cpu_percent()
        memoria_final = processo.memory_info().rss
        _, pico_memoria_modificada = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        metricas_modificada = {
            "tempo_execucao": tempo_modificada,
            "uso_cpu": (cpu_final + cpu_inicio) / 2,
            "uso_memoria": memoria_final - memoria_inicio,
            "pico_memoria": pico_memoria_modificada,
        }

        # Validação dos resultados
        resultado_correto = resultado_original == resultado_modificada
        valor_encontrado = None
        indice_correto = None

        if resultado_original != -1:
            valor_encontrado = lista[resultado_original]
            indice_correto = resultado_original == lista.index(alvo)

        return {
            "tamanho_lista": tamanho_lista,
            "alvo": alvo,
            "resultado_original": resultado_original,
            "resultado_modificada": resultado_modificada,
            "metricas_original": metricas_original,
            "metricas_modificada": metricas_modificada,
            "validacao": {
                "resultados_iguais": resultado_correto,
                "valor_encontrado": valor_encontrado,
                "indice_correto": indice_correto,
            },
        }

    @staticmethod
    def calcular_estatisticas_detalhadas(dados: pd.DataFrame) -> Dict:
        """
        Calcula estatísticas detalhadas dos resultados incluindo validação.
        """
        metricas_original = pd.DataFrame(
            [d["metricas_original"] for d in dados["metricas"]]
        )
        metricas_modificada = pd.DataFrame(
            [d["metricas_modificada"] for d in dados["metricas"]]
        )
        validacoes = [d["validacao"] for d in dados["metricas"]]

        total_testes = len(validacoes)
        testes_corretos = sum(1 for v in validacoes if v["resultados_iguais"])
        taxa_acerto = (testes_corretos / total_testes) * 100 if total_testes > 0 else 0

        return {
            "Análise de Performance": {
                "Tempo Médio Original (s)": metricas_original["tempo_execucao"].mean(),
                "Tempo Médio Modificado (s)": metricas_modificada[
                    "tempo_execucao"
                ].mean(),
                "CPU Média Original (%)": metricas_original["uso_cpu"].mean(),
                "CPU Média Modificada (%)": metricas_modificada["uso_cpu"].mean(),
                "Memória Média Original (MB)": metricas_original["uso_memoria"].mean()
                / (1024 * 1024),
                "Memória Média Modificada (MB)": metricas_modificada[
                    "uso_memoria"
                ].mean()
                / (1024 * 1024),
                "Pico de Memória Original (MB)": metricas_original["pico_memoria"].max()
                / (1024 * 1024),
                "Pico de Memória Modificada (MB)": metricas_modificada[
                    "pico_memoria"
                ].max()
                / (1024 * 1024),
            },
            "Métricas de Otimização": {
                "Redução no Tempo (%)": (
                    (
                        metricas_original["tempo_execucao"].mean()
                        - metricas_modificada["tempo_execucao"].mean()
                    )
                    / metricas_original["tempo_execucao"].mean()
                    * 100
                ),
                "Redução no Uso de CPU (%)": (
                    (
                        metricas_original["uso_cpu"].mean()
                        - metricas_modificada["uso_cpu"].mean()
                    )
                    / metricas_original["uso_cpu"].mean()
                    * 100
                ),
                "Redução no Uso de Memória (%)": (
                    (
                        metricas_original["uso_memoria"].mean()
                        - metricas_modificada["uso_memoria"].mean()
                    )
                    / metricas_original["uso_memoria"].mean()
                    * 100
                ),
            },
            "Validação": {
                "Total de Testes": total_testes,
                "Resultados Corretos": testes_corretos,
                "Taxa de Acerto": taxa_acerto,
            },
        }

    def testar_variacoes_detalhado(self) -> Tuple[Dict, Dict]:
        """
        Executa testes detalhados com paralelização e análises estatísticas.
        """
        dados_por_caso = {
            "Alvo no Início": {},
            "Alvo no Primeiro Quartil": {},
            "Alvo no Meio": {},
            "Alvo no Terceiro Quartil": {},
            "Alvo no Fim": {},
            "Alvo Inexistente": {},
            "Elemento Repetido (Primeiro)": {},
            "Elemento Repetido (Último)": {},
            "10% da Lista": {},
            "30% da Lista": {},
            "70% da Lista": {},
            "90% da Lista": {},
            "Elementos Adjacentes Iguais": {},
            "Sequência Uniforme": {},
        }

        for caso in dados_por_caso:
            dados_por_caso[caso] = {"Tamanho da Lista": [], "metricas": []}

        try:
            with ProcessPoolExecutor() as executor:
                for exp in range(1, 8):
                    tamanho_lista = 10**exp
                    print(
                        f"\n[Processando] Testando busca binária com lista de tamanho: {tamanho_lista:,} elementos"
                    )

                    # Lista base com elementos únicos
                    lista_base = sorted(
                        random.sample(range(1, tamanho_lista * 10), tamanho_lista)
                    )

                    # Lista com elementos repetidos
                    lista_repetida = lista_base.copy()
                    elemento_repetido = lista_base[len(lista_base) // 2]
                    lista_repetida[0] = elemento_repetido  # Primeiro elemento repetido
                    lista_repetida[-1] = elemento_repetido  # Último elemento repetido

                    # Lista com elementos adjacentes iguais
                    lista_adjacente = lista_base.copy()
                    pos_adjacente = len(lista_adjacente) // 3
                    lista_adjacente[pos_adjacente] = lista_adjacente[pos_adjacente + 1]

                    # Lista com distribuição uniforme
                    lista_uniforme = sorted(
                        [
                            i * (tamanho_lista * 10 // tamanho_lista)
                            for i in range(tamanho_lista)
                        ]
                    )

                    testes = []
                    casos_teste = {
                        "Alvo no Início": lista_base[0],
                        "Alvo no Primeiro Quartil": lista_base[len(lista_base) // 4],
                        "Alvo no Meio": lista_base[len(lista_base) // 2],
                        "Alvo no Terceiro Quartil": lista_base[
                            3 * len(lista_base) // 4
                        ],
                        "Alvo no Fim": lista_base[-1],
                        "Alvo Inexistente": lista_base[-1] + 1,
                        "Elemento Repetido (Primeiro)": elemento_repetido,
                        "Elemento Repetido (Último)": elemento_repetido,
                        "10% da Lista": lista_base[int(0.1 * tamanho_lista)],
                        "30% da Lista": lista_base[int(0.3 * tamanho_lista)],
                        "70% da Lista": lista_base[int(0.7 * tamanho_lista)],
                        "90% da Lista": lista_base[int(0.9 * tamanho_lista)],
                        "Elementos Adjacentes Iguais": lista_adjacente[pos_adjacente],
                        "Sequência Uniforme": lista_uniforme[len(lista_uniforme) // 2],
                    }

                    # Lista de tuplas (lista, alvo, tamanho) para cada caso
                    testes.extend(
                        [
                            (
                                lista_base.copy(),
                                casos_teste["Alvo no Início"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["Alvo no Primeiro Quartil"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["Alvo no Meio"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["Alvo no Terceiro Quartil"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["Alvo no Fim"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["Alvo Inexistente"],
                                tamanho_lista,
                            ),
                            (
                                lista_repetida.copy(),
                                casos_teste["Elemento Repetido (Primeiro)"],
                                tamanho_lista,
                            ),
                            (
                                lista_repetida.copy(),
                                casos_teste["Elemento Repetido (Último)"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["10% da Lista"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["30% da Lista"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["70% da Lista"],
                                tamanho_lista,
                            ),
                            (
                                lista_base.copy(),
                                casos_teste["90% da Lista"],
                                tamanho_lista,
                            ),
                            (
                                lista_adjacente.copy(),
                                casos_teste["Elementos Adjacentes Iguais"],
                                tamanho_lista,
                            ),
                            (
                                lista_uniforme.copy(),
                                casos_teste["Sequência Uniforme"],
                                tamanho_lista,
                            ),
                        ]
                    )

                    resultados = list(
                        executor.map(self.executar_teste_paralelo, testes)
                    )

                    for resultado, (caso, _) in zip(resultados, casos_teste.items()):
                        dados_por_caso[caso]["Tamanho da Lista"].append(tamanho_lista)
                        dados_por_caso[caso]["metricas"].append(
                            {
                                "metricas_original": resultado["metricas_original"],
                                "metricas_modificada": resultado["metricas_modificada"],
                                "validacao": resultado["validacao"],
                            }
                        )

            # Calcular estatísticas e gerar visualizações
            print("\n[Analisando] Calculando estatísticas detalhadas...")
            estatisticas = {}
            for caso, dados in dados_por_caso.items():
                estatisticas[caso] = self.calcular_estatisticas_detalhadas(
                    pd.DataFrame(dados)
                )

            # Gerar visualizações
            print("[Gerando] Criando visualizações comparativas...")
            self.plotar_analises_detalhadas(dados_por_caso)

            # Salvar resultados em Excel
            print("[Salvando] Exportando resultados detalhados para Excel...")
            with pd.ExcelWriter(
                "resultados/resultados_busca_binaria_detalhado.xlsx"
            ) as writer:
                # Estatísticas por caso
                estatisticas_df = pd.DataFrame()
                for caso, stats in estatisticas.items():
                    df_caso = pd.DataFrame.from_dict(stats, orient="index")
                    df_caso.columns = pd.MultiIndex.from_tuples(
                        [(caso, col) for col in df_caso.columns]
                    )
                    estatisticas_df = pd.concat([estatisticas_df, df_caso], axis=1)

                estatisticas_df.to_excel(writer, sheet_name="Estatísticas")

            return dados_por_caso, estatisticas

        except Exception as e:
            print(f"[ERRO] Falha durante a execução: {str(e)}")
            raise e


def main():
    """
    Função principal para executar os testes e análises.
    """
    print("=== Iniciando Análise Comparativa dos Algoritmos de Busca Binária ===")
    print("\n[Configuração] Preparando ambiente para execução dos testes...")

    analisador = BuscaBinariaAnalise()
    dados_por_caso, estatisticas = analisador.testar_variacoes_detalhado()

    print("\n=== Análise concluída com sucesso! ===")
    print("\n[Resultados] Arquivos gerados na pasta 'resultados':")
    print("1. resultados_busca_binaria_detalhado.xlsx")
    print("   └── Planilha com análise detalhada de recursos computacionais")
    print("2. analise_recursos_computacionais.png")
    print("   └── Gráficos comparativos de tempo, CPU e memória")
    print("3. comparativo_tempos_*.png")
    print("   └── Comparação detalhada de tempos por caso")
    print("4. melhorias_percentuais.png")
    print("   └── Gráfico de barras com melhorias percentuais")
    print("5. distribuicao_melhorias.png")
    print("   └── Distribuição das melhorias por caso")

    print("\n=== Resumo Detalhado por Cenário de Teste ===")
    for caso, stats in estatisticas.items():
        print(f"\n[Caso] {caso}")
        perf = stats["Análise de Performance"]
        opt = stats["Métricas de Otimização"]
        val = stats["Validação"]

        # Validação de resultados
        print(f"├── Validação dos Resultados:")
        print(f"│   ├── Testes Realizados: {val['Total de Testes']}")
        print(f"│   ├── Resultados Iguais: {val['Resultados Corretos']}")
        print(f"│   └── Taxa de Acerto: {val['Taxa de Acerto']:.2f}%")

        # Detalhes de Performance
        print(f"├── Tempo de Execução:")
        print(f"│   ├── Original: {perf['Tempo Médio Original (s)']:.6f}s")
        print(f"│   └── Modificado: {perf['Tempo Médio Modificado (s)']:.6f}s")
        print(f"├── Uso de CPU:")
        print(f"│   ├── Original: {perf['CPU Média Original (%)']:.2f}%")
        print(f"│   └── Modificado: {perf['CPU Média Modificada (%)']:.2f}%")
        print(f"├── Uso de Memória:")
        print(f"│   ├── Original: {perf['Memória Média Original (MB)']:.2f}MB")
        print(f"│   └── Modificado: {perf['Memória Média Modificada (MB)']:.2f}MB")
        print(f"└── Melhorias:")
        print(f"    ├── Redução no Tempo: {opt['Redução no Tempo (%)']:.2f}%")
        print(f"    ├── Redução no Uso de CPU: {opt['Redução no Uso de CPU (%)']:.2f}%")
        print(
            f"    └── Redução no Uso de Memória: {opt['Redução no Uso de Memória (%)']:.2f}%"
        )


if __name__ == "__main__":
    main()
