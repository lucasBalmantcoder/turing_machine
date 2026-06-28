# Simulador de Máquina de Turing

Trabalho prático da disciplina **Teoria da computação**.  
Implementação de um simulador de Máquina de Turing em Python, reconhecendo a linguagem **aⁿbⁿ**.

Equipe:

---
Lucas Patrik Lopes dos Santos - 2021015036
Salomão Marcioliver - 2020011954
Silvestre Bentes Cardoso- 2019007752
Jaiane Luana Sá Menezes - 2022004547
---


---

## ▶ Teste rápido no Google Colab

Não é necessário instalar nada. Clique no botão abaixo para abrir e executar o simulador diretamente no navegador:

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1s14jMLgSflYS5cvVJyd7N4kbURMFB3DR?hl=pt_BR#scrollTo=Q2uzqXiW5X3a)

> No Colab, basta executar as células na ordem em que aparecem. Nenhuma configuração adicional é necessária.

---

## Integrantes

| # | Nome |
|---|------|
| 1 | Pessoa 1 |
| 2 | Pessoa 2 |
| 3 | Pessoa 3 |
| 4 | Pessoa 4 |

---

## Descrição

A Máquina de Turing implementada reconhece a linguagem:

```
L = { aⁿbⁿ | n ≥ 1 }
```

Exemplos de palavras **aceitas**: `ab`, `aabb`, `aaabbb`  
Exemplos de palavras **rejeitadas**: `aab`, `ba`, `aabb b`

### Componentes formais

| Componente | Valor |
|---|---|
| **Σ** (alfabeto de entrada) | `{a, b}` |
| **Γ** (alfabeto da fita) | `{a, b, X, Y, _, *}` |
| **Q** (estados) | `{q0, q1, q2, q3, q4}` |
| **q₀** (estado inicial) | `q0` |
| **F** (estados de aceitação) | `{q4}` |
| **\_** (símbolo vazio) | `_` |
| **\*** (símbolo de início) | `*` |

### Função de transição δ

| Estado atual | Símbolo lido | Novo estado | Símbolo gravado | Direção |
|---|---|---|---|---|
| q0 | a | q1 | X | D |
| q0 | Y | q3 | Y | D |
| q1 | a | q1 | a | D |
| q1 | Y | q1 | Y | D |
| q1 | b | q2 | Y | E |
| q2 | a | q2 | a | E |
| q2 | Y | q2 | Y | E |
| q2 | X | q0 | X | D |
| q3 | Y | q3 | Y | D |
| q3 | _ | q4 | _ | D |

**Estratégia:** a cada ciclo, um `a` é marcado com `X` e o `b` correspondente com `Y`. O processo se repete até que todos os pares sejam marcados. Se a fita terminar apenas com símbolos marcados, a palavra é aceita.

---

## Como executar

### Opção 1 — Google Colab (sem instalação)

Acesse o notebook pelo link abaixo e execute as células diretamente no navegador:

🔗 [https://colab.research.google.com/drive/1s14jMLgSflYS5cvVJyd7N4kbURMFB3DR?hl=pt_BR#scrollTo=Q2uzqXiW5X3a](https://colab.research.google.com/drive/1s14jMLgSflYS5cvVJyd7N4kbURMFB3DR?hl=pt_BR#scrollTo=Q2uzqXiW5X3a)

### Opção 2 — Localmente via VS Code

**Pré-requisitos:**
- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária

**Passos:**

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/simulador-turing.git
cd simulador-turing
```

2. Execute o simulador:
```bash
python maquina_de_turing.py
```

### Testando uma palavra específica

Abra o arquivo `maquina_de_turing.py` no VS Code (ou no Colab) e altere a lista `casos_de_teste`, ou adicione ao final do arquivo:

```python
resultado = simulador.simular("aaabbb")
print(f"Resultado: {resultado}")
```

---

## Exemplo de saída

```
========================================
  SIMULADOR DE MÁQUINA DE TURING
  Linguagem: a^n b^n
========================================

Palavra testada : 'aabb'
Estado inicial  : q0
----------------------------------------
Passo 01 | Estado: q0 | Cabeçote[1]: 'a' | Fita: * a a b b _
Passo 02 | Estado: q1 | Cabeçote[2]: 'a' | Fita: * X a b b _
...
----------------------------------------
Resultado : ACEITA  |  Esperado: ACEITA  |  ✓ OK
```

---

## Ferramentas utilizadas

- **Python 3** — implementação do simulador
- **VS Code** — ambiente de desenvolvimento
- **GitHub** — versionamento e entrega do código
- **Canva** — elaboração da apresentação
- **IA (ChatGPT / Claude)** — auxílio na estruturação do código e da apresentação

---

## Estrutura do repositório

```
simulador-turing/
├── maquina_de_turing.py   # Código principal do simulador
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação
```

---

## Execução online

Caso prefira não instalar nada, o simulador também está disponível para execução direta no Google Colab:

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1s14jMLgSflYS5cvVJyd7N4kbURMFB3DR?hl=pt_BR#scrollTo=Q2uzqXiW5X3a)
