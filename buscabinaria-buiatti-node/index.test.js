const buscaBinariaBuiatti = require('./index');

describe('BuscaBinariaBuiatti', () => {
    describe('Casos básicos', () => {
        test('deve encontrar elemento em uma lista simples', () => {
            const lista = [1, 2, 3, 4, 5];
            expect(buscaBinariaBuiatti(lista, 3)).toBe(2);
        });

        test('deve retornar -1 para elemento não encontrado', () => {
            const lista = [1, 2, 3, 4, 5];
            expect(buscaBinariaBuiatti(lista, 6)).toBe(-1);
        });
    });

    describe('Casos especiais', () => {
        test('deve lidar com array vazio', () => {
            expect(buscaBinariaBuiatti([], 1)).toBe(-1);
        });

        test('deve lidar com array de um elemento', () => {
            expect(buscaBinariaBuiatti([1], 1)).toBe(0);
            expect(buscaBinariaBuiatti([1], 2)).toBe(-1);
        });

        test('deve lidar com elementos duplicados', () => {
            const lista = [1, 2, 2, 2, 3];
            const indice = buscaBinariaBuiatti(lista, 2);
            expect(lista[indice]).toBe(2);
        });
    });

    describe('Valores limite', () => {
        test('deve encontrar elementos nas bordas', () => {
            const lista = [1, 2, 3, 4, 5];
            expect(buscaBinariaBuiatti(lista, 1)).toBe(0);  // Primeiro elemento
            expect(buscaBinariaBuiatti(lista, 5)).toBe(4);  // Último elemento
        });

        test('deve lidar com valores fora dos limites', () => {
            const lista = [1, 2, 3, 4, 5];
            expect(buscaBinariaBuiatti(lista, 0)).toBe(-1);  // Menor que o menor
            expect(buscaBinariaBuiatti(lista, 6)).toBe(-1);  // Maior que o maior
        });
    });

    describe('Diferentes tipos de dados', () => {
        test('deve funcionar com strings', () => {
            const lista = ['a', 'b', 'c', 'd', 'e'];
            expect(buscaBinariaBuiatti(lista, 'c')).toBe(2);
            expect(buscaBinariaBuiatti(lista, 'f')).toBe(-1);
        });

        test('deve funcionar com números decimais', () => {
            const lista = [1.1, 2.2, 3.3, 4.4, 5.5];
            expect(buscaBinariaBuiatti(lista, 3.3)).toBe(2);
            expect(buscaBinariaBuiatti(lista, 6.6)).toBe(-1);
        });
    });

    describe('Testes de desempenho', () => {
        test('deve lidar eficientemente com arrays grandes', () => {
            const tamanho = 1000000;
            const lista = Array.from({length: tamanho}, (_, i) => i);
            
            // Teste alguns valores aleatórios
            for (let i = 0; i < 10; i++) {
                const alvo = Math.floor(Math.random() * tamanho);
                expect(buscaBinariaBuiatti(lista, alvo)).toBe(alvo);
            }
            
            // Teste valores inexistentes
            expect(buscaBinariaBuiatti(lista, -1)).toBe(-1);
            expect(buscaBinariaBuiatti(lista, tamanho)).toBe(-1);
        });
    });
});
