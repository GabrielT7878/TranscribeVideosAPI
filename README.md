
# TranscribeVideosAPI

TranscribeVideosAPI é um projeto desenvolvido em Python utilizando o framework Flask, que permite a transcrição de vídeos e geração de legendas no formato SRT para videos.





## Requisitos

- Python 3.x
- Flask
- ffmpeg
- Dependências listadas em `requirements.txt`

## Instalação

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/GabrielT7878/TranscribeVideosAPI.git
   cd TranscribeVideosAPI
   ```

2. **Crie e ative um ambiente virtual:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```sh
   pip install -r requirements.txt
   ```
   
## Requer instalações adicionais no sistema

- ffmpeg
- nvidia-cudnn no Ubuntu (sudo apt install nvidia-cudnn) - (não necessário caso for usar CPU)

## Uso

Para iniciar a aplicação Flask, execute:

```sh
python3 main.py
```

## Endpoints da API

A API fornece os seguintes endpoints:

- **/video**: Retorna um json com o campo "text" contendo o texto transcrito do vídeo.

- **/audio**: Retorna um json com o campo "text" contendo o texto transcrito do audio.

- **/srt**: Retorna um arquivo SRT de legenda do vídeo.


Por padrão, a porta do servidor é **5000**.



## Exemplo de requisição
```sh
curl --location 'http://localhost:5000/srt' \
--form 'file=@"caminho do arquivo"'
```

## Postman e Insomnia

A requisição é do tipo POST, deve ser passado no body com o tipo form-data a chave 'file', juntamente com o arquivo a ser transcrito.

![alt text](https://live.staticflickr.com/65535/53777576071_d115644f0b_c.jpg)


## Configuração

O arquivo `config.py` inclui as seguintes configurações:

- `model_size`: Especifica o tamanho do modelo Whisper (padrão: "small").

    Tamanhos de modelos disponíveis
    - **tiny**
    - **base**
    - **small**
    - **medium**
    - **large**
    
**Obs:** Quanto maior o modelo, melhor será a precisão de transcrição do modelo, porém o tempo de processamento também aumentará.
- `tempFolder`: Diretório para arquivos temporários (padrão: 'tmp').

## Exemplos de Resposta


**SRT**

![alt text](https://live.staticflickr.com/65535/53778052229_ba037f1bd7_c.jpg)

**Transcrição em Texto**

![alt text](https://live.staticflickr.com/65535/53778055994_8aaacaef14_c.jpg)

