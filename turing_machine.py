"""
Simulador de Máquina de Turing
Disciplina: Linguagens Formais e Autômatos (LFA)
Linguagem reconhecida: a^n b^n (ex: "aabb", "ab", "aaabbb")
"""


class MaquinaDeTuring:
    def __init__(
        self,
        estados,
        alfabeto,
        transicoes,
        estado_inicial,
        estados_finais,
        simbolo_vazio='_',
        simbolo_inicio='*'
    ):
        """
        Parâmetros:
            estados        (set): Conjunto de estados Q
            alfabeto       (set): Alfabeto de entrada Σ
            transicoes    (dict): Função de transição δ
                                  Formato: {(estado_atual, simbolo): (novo_estado, novo_simbolo, direcao)}
                                  Direção: 'D' = Direita, 'E' = Esquerda
            estado_inicial (str): Estado inicial q0
            estados_finais (set): Conjunto de estados de aceitação F
            simbolo_vazio  (str): Símbolo de célula vazia (padrão: '_')
            simbolo_inicio (str): Símbolo de início de fita (padrão: '*')
        """
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.simbolo_vazio = simbolo_vazio
        self.simbolo_inicio = simbolo_inicio

    def simular(self, palavra):
        """
        Simula a execução da Máquina de Turing sobre a palavra dada.

        Retorna:
            "ACEITA" se a palavra pertence à linguagem reconhecida.
            "REJEITA" caso contrário.
        """
        # Inicializa a fita: símbolo de início + palavra + células vazias
        fita = [self.simbolo_inicio] + list(palavra) + [self.simbolo_vazio] * 20
        cabecote = 1  # Começa na primeira letra da palavra (posição 1)
        estado_atual = self.estado_inicial

        print(f"Palavra testada : '{palavra}'")
        print(f"Estado inicial  : {estado_atual}")
        print("-" * 40)

        passo = 1
        while True:
            simbolo_atual = fita[cabecote]

            # Exibe configuração atual (estado, posição do cabeçote, fita)
            fita_str = ' '.join(fita).strip()
            print(f"Passo {passo:02d} | Estado: {estado_atual} | Cabeçote[{cabecote}]: '{simbolo_atual}' | Fita: {fita_str}")
            passo += 1

            # Verifica se existe transição para a configuração atual
            if (estado_atual, simbolo_atual) not in self.transicoes:
                print("-" * 40)
                if estado_atual in self.estados_finais:
                    return "ACEITA"
                else:
                    return "REJEITA"

            # Aplica a transição
            novo_estado, novo_simbolo, direcao = self.transicoes[(estado_atual, simbolo_atual)]

            # Atualiza fita e estado
            fita[cabecote] = novo_simbolo
            estado_atual = novo_estado

            # Move o cabeçote
            if direcao == 'D':
                cabecote += 1
                if cabecote >= len(fita):
                    fita.append(self.simbolo_vazio)  # Expande a fita à direita
            elif direcao == 'E':
                cabecote -= 1
                if cabecote < 0:
                    cabecote = 0  # Impede saída à esquerda da fita


# ---------------------------------------------------------------------------
# Definição da Máquina de Turing para a^n b^n
# ---------------------------------------------------------------------------

estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
alfabeto = {'a', 'b', 'X', 'Y'}
estado_inicial = 'q0'
estados_finais = {'q4'}

# Função de transição δ
# Estratégia: marcar cada 'a' com 'X' e o 'b' correspondente com 'Y',
#             alternando entre os lados da fita até não restar pares.
transicoes = {
    ('q0', 'a'): ('q1', 'X', 'D'),  # Marca 'a' com 'X', avança para encontrar 'b'
    ('q0', 'Y'): ('q3', 'Y', 'D'),  # Todos 'a' marcados; vai verificar se restam 'b'

    ('q1', 'a'): ('q1', 'a', 'D'),  # Passa por 'a' não marcado
    ('q1', 'Y'): ('q1', 'Y', 'D'),  # Passa por 'Y' (b já marcado)
    ('q1', 'b'): ('q2', 'Y', 'E'),  # Marca 'b' com 'Y', retorna ao início

    ('q2', 'a'): ('q2', 'a', 'E'),  # Volta passando por 'a'
    ('q2', 'Y'): ('q2', 'Y', 'E'),  # Volta passando por 'Y'
    ('q2', 'X'): ('q0', 'X', 'D'),  # Encontrou 'X', recomeça o ciclo

    ('q3', 'Y'): ('q3', 'Y', 'D'),  # Avança sobre os 'Y' restantes
    ('q3', '_'): ('q4', '_', 'D'),  # Fita vazia após os Y: ACEITA
}

# ---------------------------------------------------------------------------
# Execução e testes
# ---------------------------------------------------------------------------

simulador = MaquinaDeTuring(estados, alfabeto, transicoes, estado_inicial, estados_finais)

casos_de_teste = [
    ("aabb",   "ACEITA"),   # 2a, 2b → válido
    ("ab",     "ACEITA"),   # 1a, 1b → válido
    ("aaabbb", "ACEITA"),   # 3a, 3b → válido
    ("aab",    "REJEITA"),  # 2a, 1b → inválido
    ("ab",     "ACEITA"),   # reconfirma caso simples
    ("",       "REJEITA"),  # palavra vazia → inválido
]

print("=" * 40)
print("  SIMULADOR DE MÁQUINA DE TURING")
print("  Linguagem: a^n b^n")
print("=" * 40)

for palavra, esperado in casos_de_teste:
    print()
    resultado = simulador.simular(palavra)
    status = "✓ OK" if resultado == esperado else "✗ ERRO"
    print(f"Resultado : {resultado}  |  Esperado: {esperado}  |  {status}")
    print("=" * 40)
