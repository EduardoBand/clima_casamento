# *clima_casamento*

## **Introdução**

Este aplicativo foi desenvolvido para verificar a temperatura e os níveis de chuva em um determinado dia ao longo dos últimos 10 anos. A motivação para criar este projeto surgiu de um problema simples: o receio de escolher um dia chuvoso e frio para o meu casamento ao ar livre.

## **Como funciona**

O aplicativo utiliza dados históricos de condições climáticas para fornecer informações sobre temperatura e precipitação em uma localização específica ao longo dos últimos 10 anos. A interface foi construída com Streamlit, permitindo uma interação fácil e intuitiva para o usuário.

### Funcionalidades:
- Inserção de latitude e longitude da localização desejada.
- Escolha da data para verificar as condições climáticas históricas.
- Exibição de um mapa com a localização inserida.
- Tabelas e gráficos com dados diários e horários filtrados de temperatura e precipitação.

## **Como interagir**

1. **Entrada de Dados:** No painel lateral, insira a latitude e longitude da localização desejada.
2. **Escolha da Data:** Selecione a data para a qual você deseja verificar as condições climáticas.
3. **Pesquisar:** Clique no botão "Pesquisar" para obter os dados.
4. **Visualização dos Resultados:** Os dados filtrados serão exibidos em tabelas e gráficos, além de um mapa com a localização especificada.

## **Como instalar e subir**

1. Crie um ambiente virtual
```shell
conda create -n clima_casamento python=3.9
```

2. Ative o ambiente virtual
```shell
conda activate clima_casamento
```

3. Instale as seguintes bibliotecas:
```python
pip install -r requirements.txt
```

## **Como rodar**

Com o ambiente virtual ativado e todas as bibliotecas instaladas, execute o seguinte comando no seu terminal para iniciar o aplicativo Streamlit:
```python
streamlit run main.py
```

## **Estrutura do Projeto**

```python
clima_casamento/
├── app/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── data_preprocess.py
│   ├── historical_weather.py
│
├── main.py
├── README.md
├── requirements.txt
```

## **Explicação dos Arquivos Principais**

- **app/__init__.py:** Arquivo de inicialização do pacote `app`.
- **app/dashboard.py:** Contém funções para criar os elementos da interface do Streamlit, como campos de texto, tabelas, mapas e gráficos.
- **app/data_preprocess.py:** Inclui funções para criar e filtrar dataframes com os dados climáticos.
- **app/historical_weather.py:** Contém a função `get_meteo_10_years_weather_data` para obter dados históricos de clima.
- **main.py:** Script principal que executa a aplicação Streamlit e define a lógica de interação do usuário.
- **README.md:** Documento de descrição e instruções do projeto.
- **requirements.txt:** Arquivo que lista todas as bibliotecas e suas versões necessárias para rodar o projeto.

# Créditos
Desenvolvido por Eduardo Lupinetti Bandeira.

# Agradecimentos
Ao Eric Venarusso que me incentivou e, principalmente, me ensinou toda a base para a criação deste projeto, com boas práticas de programação. Obrigado, Eric <3
