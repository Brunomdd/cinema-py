# 🎬 Sistema de Reservas de Cinema

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, estruturas de dados, funções, matrizes e decomposição de problemas.

## 📋 Sobre o projeto

O sistema simula uma sala de cinema composta por:

- 8 fileiras (A até H)
- 10 assentos por fileira
- Assentos livres e ocupados
- Reserva e cancelamento de lugares
- Estatísticas da ocupação da sala

Todo o projeto foi desenvolvido em Python utilizando apenas recursos da biblioteca padrão.

---

## 🚀 Funcionalidades

- ✅ Reservar um assento
- ✅ Cancelar uma reserva
- ✅ Exibir o mapa da sala
- ✅ Mostrar estatísticas da ocupação
- ✅ Validar entradas do usuário
- ✅ Manter o estado da sala durante toda a execução

---

## 📌 Representação da sala

Cada assento é representado por uma matriz (lista bidimensional).

```
0 = Livre
1 = Ocupado
```

Visualização:

```
A O O X O O O O O O O
B O O O O O O O O O O
C O O O O O O O O O O
...
H O O O O O O O O O O
```

Legenda:

```
O = Livre
X = Ocupado
```

---

## 🛠 Conceitos utilizados

Durante o desenvolvimento foram praticados diversos conceitos de Python:

- Funções
- Matrizes (listas bidimensionais)
- Loops aninhados
- Dicionários
- Tuplas
- Retorno de funções
- Guard Clauses
- Refatoração
- Reutilização de código
- Validação de entrada
- Conversão de caracteres utilizando `ord()`
- `enumerate()`
- Organização de código em pequenas responsabilidades

---

## 📊 Estatísticas

O programa informa:

- Total de assentos
- Assentos livres
- Assentos ocupados
- Percentual de ocupação

---

## 📚 Principais aprendizados

Este projeto foi importante para compreender conceitos fundamentais de programação, como:

- Modelar um problema do mundo real utilizando uma matriz.
- Separar responsabilidades entre funções.
- Transformar entradas do usuário em índices da matriz.
- Evitar repetição de código através da criação da função `criar_indice()`.
- Entender que uma função pode retornar um único objeto (como uma tupla) contendo múltiplos valores.
- Validar corretamente entradas antes de acessar estruturas de dados.
- Refatorar código mantendo o mesmo comportamento.

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta:

```bash
cd nome-do-projeto
```

Execute:

```bash
python main.py
```

---

## 💻 Tecnologias

- Python 3

---

## 👨‍💻 Autor

**Bruno Menezes Diniz**

Estudante de Ciência da Computação, desenvolvendo projetos para praticar lógica de programação, estruturas de dados e desenvolvimento backend em Python.


## 🧠 Desafios encontrados

Durante o desenvolvimento enfrentei alguns desafios importantes:

- Representar corretamente uma sala utilizando uma matriz.
- Converter fileiras (A-H) em índices da matriz.
- Evitar recriar a sala a cada operação.
- Reutilizar código entre reserva e cancelamento.
- Compreender o retorno de funções utilizando tuplas.
- Validar corretamente entradas antes de acessar a matriz.
- Separar responsabilidades entre as funções para deixar o código mais organizado.

Cada um desses desafios contribuiu para melhorar minha compreensão sobre lógica de programação e organização de código.
