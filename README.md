<h1 align="center">
    Diário Emocional com IA
</h1>

## Sobre o projeto
Este projeto foi desenvolvido para a disciplina de Fundamentos de Inteligência Artificial, ministrada pelo professor Davi Carneiro, parte do curso de Bacharelado em Ciência da Computação do Centro Universitário de João Pessoa (Unipê). 

A aplicação atua como um Software as a Service (SaaS) que tem como objetivo principal auxiliar o controle emocional do usuário, ajudando-o a identificar e refletir sobre suas emoções. Com uma interface amigável e prática, o sistema proporciona insights com base em Inteligência Artificial.

Alunas: 
- Alessa Danúbia Barros Ferreira Duarte
- Beatriz Emmanuele Ferreira do Nascimento

### Vídeo de Apresentação
Link: Adicionar !!

### Streamlit
Link: https://diario-emocional-com-ia.streamlit.app

### Desenvolvedoras
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/100052794?v=4" width=115><br><sub>Alessa Duarte</sub>](https://github.com/alessaduarte) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/107078395?v=4" width=115><br><sub>Beatriz Emmanuele</sub>](https://github.com/BeatrizEmmanuele) | |
| :---: | :---: | :---: |

## Funcionalidades
- Análise de sentimento (positivo, neutro, negativo)
- Resumo do humor do dia
- Visualização de histórico emocional em gráficos

## Linguagens e Tecnologias Utilizadas
- Python
- Streamlit
- API do Google Gemini

## Instalação
**Dica**: Para facilitar a instalação do projeto, utilize a documentação oficial do **[Streamlit](https://docs.streamlit.io)**.

## Etapas de Instalação

### 1. Clonar o repositório

Crie uma pasta para salvar o projeto e utilize o comando: 

```bash
git clone https://github.com/BeatrizEmmanuele/ProjetoIA.git
```

### 2. Adicione a Chave de API
Para inicializar o projeto localmente, é necessário adicionar a chave diretamente ao projeto.

<p>Localize a linha de código:</p>

```bash
api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)
```

<p>Altere para:</p>

```bash
genai.configure(api_key="CHAVEDAAPI")
```

**Importante**: Modifique "**CHAVEDAAPI**" para a sua chave de API do Gemini, esse passo é fundamental para executar o projeto corretamente.

### 3. Ambiente Virtual (Venv)
Exclua a pasta "streamlit_env" do projeto.

<p>Após excluir a pasta, execute no terminal:</p>

```bash
python -m venv streamlit_env
```

<p>Ative o ambiente virtual:</p>

```bash
streamlit_env\Scripts\activate
```

### 4. Execute a Aplicação
Utilize o comando abaixo para iniciar a aplicação:

```bash
streamlit run meu_app.py
```
