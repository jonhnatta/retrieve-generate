# Nome do Projeto

## Introdução

Este projeto implementa um sistema de recuperação de argumentos utilizando a técnica de "Retrieve and Generate" (RAG). O código é capaz de extrair informações de um documento Word (no formato `.docx`) e gerar respostas baseadas nas perguntas feitas. O objetivo é facilitar a consulta a informações contidas no documento, permitindo que os usuários obtenham respostas de forma rápida e eficiente.

## Como Rodar

Para executar o projeto, siga os passos abaixo:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/jonhnatta/retrieve-generate.git
   cd retrieve-generate
   ```

2. **Instale as dependências**:
   Certifique-se de que você tem o Python e o `pip` instalados. Em seguida, instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare o documento**:
   O arquivo que você deseja fazer leitura deve estar presente na raiz do projeto. Caso você queira editar o documento:
   - Abra o arquivo deve ser do tipo `.docx`
   - Faça as alterações necessárias e salve o arquivo.

4. **Altere o código**:
5. Procure no código pela variavel `document_link` e altere para o arquivo que você colocou na raiz do projeto.
   ```python
   document_link = "./<nome_do_arquivo>.docx"  # Altere o caminho conforme necessário
   ```

6. **Configure a chave da API**:
   Crie um arquivo `.env` na raiz do projeto e adicione a seguinte linha:
   ```
   OPENAI_API_KEY=<sua_chave_api>
   ```

7. **Execute o código**:
   Após garantir que o documento está no lugar correto e que todas as dependências estão instaladas, você pode rodar o código:
   ```bash
   python main.py
   ```

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, crie um fork do repositório e envie um pull request com suas alterações.