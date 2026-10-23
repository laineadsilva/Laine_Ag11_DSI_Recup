# Controle de Níveis de Água

**Aluna:** Laine Adriele da Silva Moraes  
**Atividade:** Agenda 11 - DSI - Recuperação

Sistema em Python que simula cinco leituras de um reservatório e exibe
mensagens coloridas no terminal com a biblioteca Colorama.

## Como executar

É necessário ter Python 3 e pip instalados. Abra o terminal na pasta do projeto:

```bash
python -m pip install -r requirements.txt
python main.py
```

Em sistemas que utilizam o comando python3, substitua python por python3.
Execute em um terminal com suporte a cores ANSI. Visualizadores de texto e
alguns consoles podem não mostrar as cores.

## Níveis simulados

| Nível | Situação | Cor |
| --- | --- | --- |
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

O programa percorre a lista de níveis de 1 a 5. Cada linha representa a
situação atual em uma leitura da simulação; não são leituras de um sensor real.

## Organização do código

- `definir_cor(nivel)`: valida o nível e retorna sua cor.
- `exibir_situacao(nivel)`: consulta a lista de mensagens e exibe a situação.
- `main()`: inicializa Colorama e executa a simulação.

O índice `nivel - 1` permite associar os níveis 1 a 5 às posições 0 a 4
das listas. A expressão `Style.RESET_ALL` restaura o estilo padrão após
cada mensagem. Níveis inválidos geram um erro claro.

As cores seguem a tabela do enunciado. Não foram definidos percentuais
ou limites físicos porque a atividade solicita níveis simbólicos.

## Exemplo de saída

```text
CONTROLE DE NÍVEIS DE ÁGUA
Simulação: cada linha representa uma leitura do reservatório.

Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)
```

No terminal compatível, as cinco mensagens aparecem nas cores da tabela.

## Arquivos

- `main.py`: código completo comentado.
- `requirements.txt`: dependência necessária.
- `README.md`: explicação e instruções de execução.
- `.gitignore`: ignora arquivos temporários do Python.

## Publicação no GitHub

1. Extraia o ZIP caso tenha recebido o projeto compactado.
2. Crie um repositório com o nome `Laine_Ag11_DSI_Recup`.
3. Na página do repositório, use **Add file > Upload files** e envie os
   arquivos da pasta, mantendo `main.py`, `requirements.txt` e `README.md`
   na raiz do repositório.
4. Confirme o envio em **Commit changes**.
5. Copie o endereço real do repositório e envie no fichário da atividade.

Não envie somente o ZIP ao repositório: os arquivos do projeto devem estar
disponíveis para leitura.
