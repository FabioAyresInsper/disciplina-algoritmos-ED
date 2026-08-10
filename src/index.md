---
title: Algoritmos e Estruturas de dados
subtitle: 2026.2
...

# Avisos

**09/02**: Nesta disciplina, é proibida a utilização de ferramentas e plugins de IA generativa (IAg) em todas as atividades, pois a avaliação dos objetivos de aprendizagem é baseada no raciocínio lógico do próprio aluno.

**Links importantes**:

- [Avisos (blackboard)](https://insper.blackboard.com/ultra/courses/_52846_1/announcements)
- [Exercícios (prairie learn)](https://us.prairielearn.com/pl/course_instance/211219)
- [Plano de aulas](./plano-de-aulas.xlsx)

# Equipe

::: equipe :::

- ![](css/igor.png) Igor Montagner
- ![Ana](css/ana-helena.jpeg) Ana Helena Caiafa (2025)
- ![](css/ian.jpeg) Ian Cordibello Desponds (2025/01)
- ![](css/livia.jpg) Lívia Tanaka (2024/02)
- ![](css/vaz.jpg) Eduardo Vaz (2024/02)
:::

# Avaliações

Teremos os seguinte itens de avaliação

- $PL$ - média de todos os exercícios no PrairieLearn
- $P1$ - prova de árvores
- $P2$ - prova de grafos

A nota final $NF$ é calculada da seguinte maneira.

$$
NF = 0.25 \times PL + P1 \times 0.3 + P2 \times 0.45
$$

Com a condição de que $(P1 + 2 \times P2)/3 \geq 4.5$.

# Como usar o material

Nossas aulas estão divididas em 3 materiais principais:

1. **slides** usados nas partes expositivas das aulas.
2. **handouts** contendo atividades feitas em aula e explicações adicionais. Estão em formato PDF. É possível usar tanto impresso quanto anotando o PDF digitalmente.
3. **exercícios conceituais** no PrairieLearn específicos para cada aula.

Veja os vídeos abaixo para entender um pouco melhor a mudança para material impresso e também algumas dicas de como aproveitar melhor esse tipo de material. Temos tanto para uso em papel como digital via anotações no PDF.

<a class="button" href="https://youtu.be/8eoDvbbxYhE">Uso do material em Papel</a> <!-- <a class="button" href="#">Uso do material em PDF</a> -->

Além disso, também teremos exercícios de implementação gerais de cada assunto. Eles são listados no início de cada assunto.

1. **implementação** dos algoritmos no PrairieLearn. Objetivo é traduzir os algoritmos vistos em sala para *C*.
2. **exercícios extras** em sites como LeetCode, hackerrank e etc. Úteis para praticar para prova e ter mais exemplos dos algoritmos e estruturas de dados sendo usados.

# Aulas

<center><object data="slides-inicio.pdf" width="400" height="300"></object></center>

Atividades de aula estão organizadas em grandes tópicos que serão abordados em mais de uma aula. As atividades esperadas de cada dia estão listadas dentro de cada tópico.

## Introdução a Programação em C

Os materiais iniciais estão no site dos [Labs de C](https://insper.github.io/Labs-de-C).

**Alocação de memória**: [handout](01-c/handout.pdf) / [slides](01-c/slides.pdf) / [PrairieLearn][pl-malloc]

[pl-malloc]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651609

## Árvores Binárias de Busca

| Aula          | Slides                                        | Handout                                  | Exercícios                          |
|---------------|-----------------------------------------------|------------------------------------------|-------------------------------------|
| Introdução    | [Baixar](02-abb-intro/slides-intro.pdf)       | [Baixar](02-abb-intro/handout-intro.pdf) | [Acessar][exercicios-intro-abb]     |
| Inserção      |                                               | [Handout](03-abb-insere/handout.pdf)     | [Acessar][exercicios-insere-abb]    |
| Balanceamento | [Slides](04-abb-balance/slides.pdf)           | [Handout](04-abb-balance/handout.pdf)    | [Acessar][exercicios-balanceia-abb] |
| Remoção       | [Video Rotação](https://youtu.be/YzSuUj54Mo0) | [Handout](05-abb-remove/handout.pdf)     | [Acessar][exercicios-remove-abb]    |
|               |                                               |                                          |                                     |

[exercicios-intro-abb]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651602
[exercicios-insere-abb]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651601
[exercicios-balanceia-abb]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651600
[exercicios-remove-abb]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651603

### Exercícios extras

Os seguintes exercícios do leetcode são interessantes e relacionados ao assunto atual.

1. (**BÁSICO**)[Soma de caminho até folha](https://leetcode.com/problems/path-sum/)
2. (**BÁSICO**)[Soma K](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
3. (**BÁSICO**)[Altura mínima](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
4. (**MÉDIO**)[Convertendo array ordenado em árvore](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
5. Leetcode 101.  Symmetric Tree
6. Leetcode 129. Sum Root to Leaf numbers
7. Leetcode 199. Right view of tree
8. Leetcode 257. Binary tree paths (fazer em Python)

## Grafos

| Aula                                | Materiais                                                                         | Exercícios                                             |
| --                                  | ---                                                                               | ---                                                    |
| Introdução                          | [Slides](06-grafos-intro/slides.pdf) / [Handout](06-grafos-intro/handout.pdf)     | [Acessar][exercicios-grafos-basicos]                   |
| Representação Computacional         | [Handout](06-grafos-intro/handout-repr-computacional.pdf)                         | [Acessar][exercicios-grafos-repr]                      |
| Componentes conexos                 | [Slides](07-dfs/slides.pdf) / [Handout](07-dfs/handout.pdf)                       | [Acessar][exercicios-grafos-dfs]                       |
| Caminhos mínimos                    | [Slides](08-bfs/slides.pdf) / [Handout](08-bfs/handout.pdf)                       |[Acessar][exercicios-grafos-bfs]                        |
| Caminhos mínimos com pesos          | [Slides](09-dijkstra/slides.pdf) / [Handout](09-dijkstra/handout.pdf)             |[Acessar][exercicios-grafos-dijkstra]                   |

[exercicios-grafos-basicos]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651605
[exercicios-grafos-repr]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651604
[exercicios-grafos-dfs]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651607
[exercicios-grafos-bfs]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651606
[exercicios-grafos-dijkstra]: https://us.prairielearn.com/pl/course_instance/211219/assessment/2651608

### Exercícios extras

Os seguintes exercícios do leetcode são interessantes e relacionados ao assunto atual.

**Básicos**:

- [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
- [Star Graphs](https://leetcode.com/problems/find-center-of-star-graph/)
- [Town Judge](https://leetcode.com/problems/find-the-town-judge/)
**Busca em Profundidade**:

- [Course Schedule](https://leetcode.com/problems/course-schedule/description/)
- [Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
- [Is graph bipartite](https://leetcode.com/problems/is-graph-bipartite/description/)

**Busca em Largura**:

- [Flood fill](https://leetcode.com/problems/flood-fill/description/)
- [Island perimeter](https://leetcode.com/problems/island-perimeter/description/)
- [01 Matrix](https://leetcode.com/problems/01-matrix/description/)

**Dijkstra**:

- [findTheCity](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/)
- [Network Delay](https://leetcode.com/problems/network-delay-time/description/)

# Materiais antigos

Aqui está o material completo usado em cada ano nesta disciplina.

- [2025/01](old/2025-1.zip)
