# 🎥 Video to DOCX Transcription App

![App Screenshot](https://github.com/VitorCamposAds/VideoToDocs_img/blob/main/VideoToDocx.png?raw=true)

## 🌟 Descrição

A **Video to DOCX Transcription App** é uma aplicação poderosa que permite extrair áudio de arquivos de vídeo e transcrever o conteúdo em um documento Word (.docx). Utilizando a biblioteca Whisper para transcrição e PyQt5 para a interface gráfica, esta ferramenta é perfeita para transformar vídeos em texto de forma rápida e eficiente.

## 🚀 Funcionalidades

- **Extração de Áudio**: Converte arquivos de vídeo em arquivos de áudio.
- **Transcrição de Áudio**: Transcreve o áudio extraído para texto.
- **Exportação para DOCX**: Salva a transcrição em um documento Word.
- **Interface Gráfica**: Interface amigável e moderna para facilitar o uso.

## 🛠️ Instalação

Siga os passos abaixo para configurar o ambiente e executar a aplicação:

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie um Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Baixe o Modelo Whisper:**
    ```python
    import whisper
    modelo = whisper.load_model("small")
    ```

## 🎮 Uso

1. **Execute a Aplicação:**
    ```bash
    python seu_arquivo.py
    ```

2. **Selecione o Arquivo de Vídeo:**
    - Clique no botão "Procurar" e escolha o arquivo de vídeo que deseja transcrever.

3. **Escolha o Local para Salvar:**
    - Clique no botão "Escolher Local para Salvar" e selecione onde deseja salvar o documento transcrito.

4. **Adicione um Título:**
    - Insira o título desejado para o documento.

5. **Clique em "Processar":**
    - A aplicação irá extrair o áudio, transcrever e salvar no formato DOCX.

## 📚 Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada.
- **PyQt5**: Para a interface gráfica.
- **Whisper**: Biblioteca para transcrição de áudio.
- **python-docx**: Para manipulação de documentos Word.
- **FFmpeg**: Para extração de áudio dos vídeos.


## Dependências

Para executar este projeto, você precisa do `ffmpeg.exe`. Devido ao seu tamanho (135 MB), não foi possível incluí-lo diretamente no repositório do GitHub, que tem um limite de 100 MB por arquivo. Portanto, você pode baixá-lo [aqui](https://drive.google.com/file/d/1fGjIiQFJBR3MXM0DpI4QzRSAcATQR-aU/view?usp=sharing).

### Instruções para Download

1. Clique no link acima para acessar o arquivo.
2. Faça o download e coloque o `ffmpeg.exe` na mesma pasta que o script do projeto.

---

<p align="center">
    Feito com ❤️ por <a href="https://github.com/VitorCamposAds">Vitor Campos Moura Costa</a>
</p>
