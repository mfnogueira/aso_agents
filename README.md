# Projeto Aso Agents

![CrewAI Logo](https://github.com/joaomdmoura/crewAI/blob/main/docs/crewai_logo.png?raw=true)

Este projeto utiliza a biblioteca CrewAI para automatizar a escrita de artigos utilizando linguagem natural e ferramentas de scraping.

## Configuração Inicial

Antes de começar, siga os passos abaixo para configurar o ambiente:

1. Acesse o site [groq.com](https://groq.com) e gere uma chave de API. Esta chave será utilizada no arquivo `.env`. O modelo utilizado é o `lhama3-8b-8192`.

2. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes linhas, substituindo `<sua_chave_api>` pela chave API gerada:

   ```plaintext
   GROQ_API_KEY=<sua_chave_api>
   MODEL=llama3-8b-8192

Isso permite que o script main.py acesse a API do Groq com a chave apropriada.

Instalação dos Pacotes Necessários
Para instalar os pacotes necessários, utilize o seguinte comando:

pip install -r requirements.txt

Certifique-se de estar no diretório raiz do projeto ao executar este comando.

Executando o Script
Para executar o script main.py, utilize o Python 3.x com o seguinte comando:

python main.py

