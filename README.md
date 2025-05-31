# MBA-HousesPrice
# Análise de Preços de Casas - Ames, Iowa

Este repositório contém uma análise exploratória dos preços de venda de casas em Ames, Iowa, utilizando **Python**, **Streamlit** e bibliotecas de visualização como **Seaborn**, **Plotly** e **Matplotlib**. O foco está em como diferentes características dos imóveis influenciam o valor final de venda, trazendo insights relevantes sobre o mercado imobiliário local.

---

## Visão Geral

Através de um dataset com informações de **1.460 imóveis**, investigamos como fatores como:

- Qualidade da construção
- Características dos bairros
- Acabamento do porão

impactam no preço de venda das casas. O objetivo é entender **quais elementos mais influenciam** na precificação dos imóveis.

---

## Objetivos da Análise

- **Distribuição de Preços:** Explorar a distribuição dos valores de venda e identificar os principais fatores de impacto.
- **Correlação de Características:** Analisar quais variáveis possuem maior correlação com o preço de venda.
- **Preço por Metro Quadrado:** Observar a influência da localização sobre o preço médio por metro quadrado nos bairros.

---

## Tecnologias Utilizadas

- **Python:** Linguagem principal para a análise e visualizações.
- **Streamlit:** Framework para construção do dashboard interativo.
- **Pandas:** Manipulação de dados tabulares.
- **Seaborn / Matplotlib:** Visualizações estatísticas e gráficos estáticos.
- **Plotly:** Gráficos interativos e exploratórios.

---

## Funcionalidades

- **Filtro de Bairros:** Selecione bairros específicos ou visualize todos os dados ao escolher "Todos".
- **Distribuição de Preços:** Gráfico interativo que mostra a variação e outliers nos preços de venda.
- **Correlação com o Preço:** Quais variáveis mais impactam o preço de venda.
- **Preço Médio por m²:** Avaliação interativa dos preços médios por metro quadrado por bairro.

---

## Como Executar

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/repo-analisepreco-casas.git
cd repo-analisepreco-casas
```

### 2. Instale as Dependências
Certifique-se de ter o Python 3.7+ instalado. Depois, execute:

```bash
pip install -r requirements.txt
```

### 3. Execute a Aplicação
Inicie o dashboard com:

```bash
streamlit run app.py
```
A aplicação será aberta automaticamente no seu navegador.

---

## Exemplos de Visualizações
### 1. Distribuição de Preços de Venda
Gráfico com a frequência de preços de venda, destacando padrões e possíveis outliers.

### 2. Correlação com o Preço
Visualização das variáveis mais influentes no preço final, como:
- Qualidade da construção (OverallQual)
- Acabamento do porão (BsmtQual)

### 3. Preço Médio por Metro Quadrado
Mapa interativo ou gráfico de barras mostrando os bairros com os maiores e menores valores por m².

---

## Resultados e Insights
- Tamanho não é tudo: Qualidade de acabamento e porão têm impacto maior que a área total.
- Localização é essencial: Bairros como NridgHt e StoneBr têm os maiores preços por m².
- Construção e acabamento: Casas com melhores acabamentos podem valer até o dobro de outras similares.

## Conclusão
Este projeto demonstra como a análise de dados pode revelar padrões relevantes no mercado imobiliário. Além de identificar as variáveis mais relevantes na formação de preços, ele oferece uma visão detalhada por localização.

Explore o dashboard e descubra o que realmente valoriza um imóvel em Ames, Iowa.

---

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
