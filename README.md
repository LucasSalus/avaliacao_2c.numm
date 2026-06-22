# avaliacao_2c.numm
Repositório para a segunda avaliação da disciplina de Cálculo Numérico do professor Lucas Reis.

Objetivo do projeto de traduzir em formulas computacionais, lógicas de funcionamento e calculo de forma eficiente, sem uso de bibliotecas immportadas.

Alunos:
Lucas Salustriano dos Santos 
Willian Santos Pinheiro 

Histórico de implementação
Commit 1: Estrutura inicial e método de Lagrange.
- Criada a arquitetura básica da biblioteca de interpolação em 'interpolacao.py'.
- Implementado o algoritmo de Interpolação Polinomial de Lagrange usando apenas laços nativos.
- Desenvolvido o arquivo 'main.py' com o caso de teste prático para o Problema 1 (Telemetria do Drone)
  
Commit seguinte a inclusão inicial: Inclusão do método de Newton.
- Adicionada a função 'interpolacao_newton' ao módulo de interpolação.
- Implementada a construção da tabela de diferenças divididas usando estruturas nativas.
- Finalizada a primeira parte do projeto (Problema 1 - Telemetria do Drone).
Implementação seguinte.
- Adicionado o caso de teste do Problema 2 (Data Center) com Gregory-Newton.
- Adicionado o caso de teste do Problema 3 (Braço Robótico) avaliando Spline Linear e Cúbica Natural.
- Atualizados os imports do módulo 'interpolacao'.
Atualização seguinte:
- Criação da biblioteca de integração.py.
- Incluído o import do módulo 'integracao'.
- Adicionado o bloco de testes para o Problema 4 (Integração Numérica).
- Configurada a chamada simultânea das regras de Newton-Cotes para validação dos resultados.
Próxima implementação:
- Corrigidos todos os datasets de teste com base nas especificações finais do PDF.
- Implementado o Ajuste Linear por Mínimos Quadrados (MMQ) para previsão de tráfego.
- Desenvolvida a Quadratura de Gauss com n=2 pontos para integração de funções contínuas.
- Projeto totalmente finalizado atendendo aos requisitos da Unidade 2.
