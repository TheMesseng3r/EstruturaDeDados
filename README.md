# Estrutura de Dados

**AVALIAÇÃO DE NOTAÇÃO POSFIXA**

O objetivo deste trabalho é implementar um programa que receba um arquivo com uma sequência de expressões numéricas em notação posfixa e avaliar cada uma destas expressões, imprimindo o resultado da expressão ou uma mensagem de erro adequada. Cada uma das expressões é dada por uma string onde cada operando numérico é finalizado com um ponto para evitar ambiguidades. Um exemplo de uma destas expressões é dado abaixo:

    98765.76543.-54321.32109.-

Seu programa deve abrir o arquivo de teste e avaliar cada uma das expressões (uma expressão por linha). Para cada uma delas, imprimir uma saída (resultado ou mensagem de erro). Os operandos na expressão devem ser convertidos para inteiro antes de serem processados. Para simplificar, a operação de divisão deve ter por resultado somente a parte inteira da divisão. A avaliação da expressão deve utilizar o tipo abstrato de dados Pilha (com implementação estática em vetor, conforme visto em sala de aula e constante no material de estudo – slides). Na implementação da Pilha, é vedado o uso de quaisquer funções prontas da linguagem. Você deve implementar como consta nos slides.

Em relação às mensagens de erro, informar quando:

* Estiver faltando um operando;
* Estiver faltando um operador;

* For uma divisão por zero.

	O programa deve ser implementado em Python 3.x. O programa deve permitir a escolha do arquivo de teste. Um arquivo de teste está disponível com este enunciado. Devem ser entregues em um arquivo .zip todos os arquivos de sua implementação. Certifique-se que seu programa execute com todos os arquivos necessários na mesma pasta/diretório. 

A nota do Primeiro Trabalho será dada à implementação do tipo Pilha, conforme os slides. 

A nota do Segundo Trabalho será dada à implementação da solução posfixa solicitada. O trabalho pode ser feito individualmente ou em dupla.
