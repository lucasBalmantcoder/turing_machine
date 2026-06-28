class MaquinaDeTuring:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais, simbolo_vazio='_', simbolo_inicio='*'):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # Formato: {(estado_atual, simbolo_atual): (novo_estado, novo_simbolo, direcao)}
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.simbolo_vazio = simbolo_vazio
        self.simbolo_inicio = simbolo_inicio

    def simular(self, palavra):
        # Inicializa a fita com o símbolo de início, a palavra e símbolos vazios extras
        fita = [self.simbolo_inicio] + list(palavra) + [self.simbolo_vazio] * 20
        cabecote = 1  # Inicia na primeira letra da palavra (índice 1)
        estado_atual = self.estado_inicial

        print(f"Palavra inicial: {palavra}")
        print(f"Estado inicial: {estado_atual}\n")

        while True:
            simbolo_atual = fita[cabecote]

            # Verifica se existe transição mapeada para a configuração atual
            if (estado_atual, simbolo_atual) not in self.transicoes:
                if estado_atual in self.estados_finais:
                    return "ACEITA"
                else:
                    return "REJEITA"

            # Aplica a transição
            novo_estado, novo_simbolo, direcao = self.transicoes[(estado_atual, simbolo_atual)]

            # Atualiza a fita e o estado
            fita[cabecote] = novo_simbolo
            estado_atual = novo_estado

            # Movimenta o cabeçote (D = Direita, E = Esquerda)
            if direcao == 'D':
                cabecote += 1
                if cabecote >= len(fita):
                    fita.append(self.simbolo_vazio)  # Expande a fita à direita se necessário
            elif direcao == 'E':
                cabecote -= 1
                if cabecote < 0:
                    cabecote = 0  # Impede que o cabeçote saia da fita à esquerda

# --- EXEMPLO DE USO ---
# Exemplo: Máquina que aceita a linguagem a^n b^n (ex: "aabb")

estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
alfabeto = {'a', 'b', 'X', 'Y'}
estado_inicial = 'q0'
estados_finais = {'q4'}

# Definição da função de transição delta
transicoes = {
    ('q0', 'a'): ('q1', 'X', 'D'),  # Marca 'a' com 'X', vai para q1
    ('q0', 'Y'): ('q3', 'Y', 'D'),  # Se encontrar 'Y', vai para q3 verificar fim

    ('q1', 'a'): ('q1', 'a', 'D'),  # Passa por 'a'
    ('q1', 'Y'): ('q1', 'Y', 'D'),  # Passa por 'Y'
    ('q1', 'b'): ('q2', 'Y', 'E'),  # Marca 'b' com 'Y', vai para q2 e volta

    ('q2', 'a'): ('q2', 'a', 'E'),  # Volta por 'a'
    ('q2', 'Y'): ('q2', 'Y', 'E'),  # Volta por 'Y'
    ('q2', 'X'): ('q0', 'X', 'D'),  # Encontra 'X', volta para q0 e avança

    ('q3', 'Y'): ('q3', 'Y', 'D'),  # Passa por 'Y'
    ('q3', '_'): ('q4', '_', 'D')   # Se encontrar o vazio, aceita
}

# Instanciação do simulador
simulador = MaquinaDeTuring(estados, alfabeto, transicoes, estado_inicial, estados_finais)

# Teste com uma palavra
resultado = simulador.simular("aabb")
print(f"Resultado do teste: {resultado}")
