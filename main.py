import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Análise de Preços de Casas", layout="wide")
st.title("Análise de Preços de Venda de Casas")



# Estilo customizado para alterar os chips rosa no sidebar para azul
st.markdown(
    """
    <style>
    /* Altera a cor dos chips de multiselect no sidebar */
    section[data-testid="stSidebar"] .css-1n76uvr, /* chips padrão */
    section[data-testid="stSidebar"] .css-1r6slb0 {
        background-color: #1f77b4 !important; /* azul plotly */
        color: white !important;
        border: none !important;
    }

    /* Caso algum outro estilo específico esteja sendo aplicado */
    section[data-testid="stSidebar"] .stMultiSelect span {
        background-color: #1f77b4 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Carregar e renomear os dados
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    rename_dict = {
        'Id': 'Id',
        'MSSubClass': 'TipoClasseMS',
        'MSZoning': 'ZonaMS',
        'LotFrontage': 'FrenteTerreno',
        'LotArea': 'AreaTerreno',
        'Street': 'Rua',
        'Alley': 'Beco',
        'LotShape': 'FormatoTerreno',
        'LandContour': 'ContornoTerreno',
        'Utilities': 'Utilidades',
        'LotConfig': 'ConfigTerreno',
        'LandSlope': 'InclinacaoTerreno',
        'Neighborhood': 'Bairro',
        'Condition1': 'Condicao1',
        'Condition2': 'Condicao2',
        'BldgType': 'TipoEdificacao',
        'HouseStyle': 'EstiloCasa',
        'OverallQual': 'QualidadeGeral',
        'OverallCond': 'CondicaoGeral',
        'YearBuilt': 'AnoConstrucao',
        'YearRemodAdd': 'AnoReforma',
        'RoofStyle': 'EstiloTelhado',
        'RoofMatl': 'MaterialTelhado',
        'Exterior1st': 'RevestimentoExt1',
        'Exterior2nd': 'RevestimentoExt2',
        'MasVnrType': 'TipoRevestimentoMuro',
        'MasVnrArea': 'AreaRevestimentoMuro',
        'ExterQual': 'QualidadeExterna',
        'ExterCond': 'CondicaoExterna',
        'Foundation': 'Fundacao',
        'BsmtQual': 'QualidadePorao',
        'BsmtCond': 'CondicaoPorao',
        'BsmtExposure': 'ExposicaoPorao',
        'BsmtFinType1': 'TipoAcabamentoPorao1',
        'BsmtFinSF1': 'AreaAcabamentoPorao1',
        'BsmtFinType2': 'TipoAcabamentoPorao2',
        'BsmtFinSF2': 'AreaAcabamentoPorao2',
        'BsmtUnfSF': 'AreaPoraoNaoAcabado',
        'TotalBsmtSF': 'AreaTotalPorão',
        'Heating': 'Aquecimento',
        'HeatingQC': 'QualidadeAquecimento',
        'CentralAir': 'ArCondicionadoCentral',
        'Electrical': 'SistemaEletrico',
        '1stFlrSF': 'Area1Andar',
        '2ndFlrSF': 'Area2Andar',
        'LowQualFinSF': 'AreaBaixaQualidade',
        'GrLivArea': 'AreaUtil',
        'BsmtFullBath': 'BanheiroCompletoPorao',
        'BsmtHalfBath': 'LavaboPorao',
        'FullBath': 'BanheirosCompletos',
        'HalfBath': 'Lavabos',
        'BedroomAbvGr': 'QuartosAcimaSolo',
        'KitchenAbvGr': 'CozinhasAcimaSolo',
        'KitchenQual': 'QualidadeCozinha',
        'TotRmsAbvGrd': 'ComodosAcimaSolo',
        'Functional': 'Funcionalidade',
        'Fireplaces': 'Lareiras',
        'FireplaceQu': 'QualidadeLareira',
        'GarageType': 'TipoGaragem',
        'GarageYrBlt': 'AnoGaragem',
        'GarageFinish': 'AcabamentoGaragem',
        'GarageCars': 'VagasGaragem',
        'GarageArea': 'AreaGaragem',
        'GarageQual': 'QualidadeGaragem',
        'GarageCond': 'CondicaoGaragem',
        'PavedDrive': 'EntradaPavimentada',
        'WoodDeckSF': 'AreaDeckMadeira',
        'OpenPorchSF': 'AreaVarandaAberta',
        'EnclosedPorch': 'AreaVarandaFechada',
        '3SsnPorch': 'AreaVaranda3Estacoes',
        'ScreenPorch': 'AreaVarandaTela',
        'PoolArea': 'AreaPiscina',
        'PoolQC': 'QualidadePiscina',
        'Fence': 'Cerca',
        'MiscFeature': 'OutrasCaracteristicas',
        'MiscVal': 'ValorOutrosItens',
        'MoSold': 'MesVenda',
        'YrSold': 'AnoVenda',
        'SaleType': 'TipoVenda',
        'SaleCondition': 'CondicaoVenda',
        'SalePrice': 'PrecoVenda'
    }
    df = df.rename(columns=rename_dict)
    return df

df = load_data()
# Sidebar com filtros
st.sidebar.header("Filtros")



# Adiciona a opção 'Todos' no multiselect de bairros
all_neighborhoods = ['Todos'] + df['Bairro'].dropna().unique().tolist()

selected_zone = st.sidebar.multiselect(
    "Zonas residenciais (ZonaMS):",
    options=df['ZonaMS'].dropna().unique(),
    default=df['ZonaMS'].dropna().unique()
)

selected_neighborhood = st.sidebar.multiselect(
    "Bairros:",
    options=all_neighborhoods,
    default=[]
)
# Lógica para selecionar todos os bairros se 'Todos' for escolhido
if 'Todos' in selected_neighborhood:
    selected_neighborhood = df['Bairro'].dropna().unique().tolist()




# Aplicar filtros
filtered_df = df[(df['ZonaMS'].isin(selected_zone)) & (df['Bairro'].isin(selected_neighborhood))]
# Seção 1: Visão Geral
st.subheader('"Quanto vale o seu lar?" — Uma viagem pelo mercado de casas de Ames, Iowa')
st.write("Imagine uma cidade em transformação, onde cada casa guarda uma história — e um preço que diz muito mais do que parece. Em Ames, Iowa, exploramos 1.460 lares, desvendando como estrutura, localização e detalhes escondidos constroem o valor de mercado.")
#st.dataframe(filtered_df.head())

# Seção 2: Distribuição dos Preços de Venda
#st.subheader("2. Distribuição do Preço de Venda")
st.subheader('Bloco a bloco: O que realmente pesa no valor de uma casa? Será que o tamanho é tudo? Ou um porão bem-acabado pode fazer toda a diferença?')
st.write('Descobrimos que:')
st.write('Casas com acabamento de alto padrão (OverallQual) chegam a valer o dobro das comuns.')
st.write('Um porão finalizado não é só conforto — é também um investimento.')
st.write('Garagens amplas e lareiras charmosas elevam o preço final mais do que um grande quintal.')

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.histplot(filtered_df["PrecoVenda"], kde=True, bins=30, ax=ax1, color='skyblue')
ax1.set_title("Distribuição dos Preços de Venda")
ax1.set_xlabel("Preço de Venda")
st.pyplot(fig1)


# Seção 3: Correlação com o Preço
st.subheader("Caracteristicas que mais influenciam no Preço de Venda")
st.write('Use o filtro ao lado para visualizar apenas os fatores de *Alta, **Média* ou *Baixa* influência. Isso ajuda a entender *O que mais pesa na precificação de um imóvel*.')
#corr = filtered_df.select_dtypes(include='number').corr()
#top_corr = corr["PrecoVenda"].sort_values(ascending=False)[1:11]
#st.bar_chart(top_corr)

# Função para classificar os níveis de correlação
def nivel_influencia(valor):
    valor_abs = abs(valor)
    if valor_abs >= 0.6:
        return "Alta"
    elif valor_abs >= 0.4:
        return "Média"
    else:
        return "Baixa"

# Calcular correlação com PrecoVenda
corr = filtered_df.select_dtypes(include='number').corr()['PrecoVenda'].drop('PrecoVenda')
corr_df = corr.to_frame(name='Correlação')
corr_df['Influência'] = corr_df['Correlação'].apply(nivel_influencia)

# Filtro interativo via radio
nivel = st.radio("Selecione o nível de influência:", ["Alta", "Média", "Baixa"])

# Filtrar e mostrar gráfico
filtradas = corr_df[corr_df['Influência'] == nivel]

if not filtradas.empty:
    st.bar_chart(filtradas['Correlação'])
else:
    st.info("Nenhuma variável com esse nível de influência.")



# Seção 4: Preço médio por metro quadrado por bairro
st.subheader("O poder do CEP: localização vale ouro. Nem todo bairro é igual.")
st.write('"NridgHt" e "StoneBr" aparecem no topo, com os valores mais altos por metro quadrado — mesmo em imóveis menores ou mais antigos, a localização agrega valor."')
st.write('Outros bairros com destaque incluem "NoRidge" e "Veenker", reforçando o efeito de prestígio e infraestrutura.')
st.write('Já bairros como "MeadowV" e "IDOTRR" mostram baixo valor por m², o que pode indicar menor atratividade, infraestrutura mais básica ou maior oferta que demanda.')

# Calcular o preço por metro quadrado
filtered_df = filtered_df.copy()
filtered_df = filtered_df[filtered_df['AreaUtil'] > 0]  # Evita divisão por zero
filtered_df['Preco_m2'] = filtered_df['PrecoVenda'] / filtered_df['AreaUtil']

# Calcular média por bairro
media_m2_bairro = filtered_df.groupby('Bairro')['Preco_m2'].mean().sort_values(ascending=False).reset_index()

# Criar gráfico de barras
fig_m2 = px.bar(
    media_m2_bairro,
    x='Bairro',
    y='Preco_m2',
    title='Preço médio por metro quadrado por Bairro',
    labels={'Preco_m2': 'Preço por m² (R$)', 'Bairro': 'Bairro'},
    color='Preco_m2',
    color_continuous_scale='Blues'  # Alterado para a escala de cores azul
)

fig_m2.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_m2, use_container_width=True)


st.subheader('Conclusão: muito além de tijolos e cimento')
st.write('O valor de uma casa é mais do que a soma dos seus quartos, banheiros e metros quadrados. É também um reflexo do lugar onde ela está, do status que carrega e das decisões urbanas que moldam a cidade. Ames, com seus bairros tão diversos, mostra que o CEP é tão valioso quanto o próprio imóvel — e às vezes, até mais.')
st.write('Nossa jornada por esses 1.460 lares revelou um mercado onde a localização dita o preço, onde bairros como NridgHt e StoneBr concentram o alto valor por m² mesmo em casas modestas, enquanto outras regiões oferecem mais espaço por menos.')
st.write('Ao cruzar área, estrutura e vizinhança, percebemos que os dados contam histórias que o olho nu não vê. Eles nos ajudam a entender a lógica — e às vezes a injustiça — por trás da precificação urbana.')
st.write('Seja para um comprador, corretor, urbanista ou pesquisador, essa análise mostra o poder dos dados para trazer clareza ao que parece apenas intuição. Porque no fim das contas, toda casa conta uma história — e todo bairro, um capítulo diferente da mesma cidade.')
